import numpy as np
import re
import operator
from tqdm import tqdm

class Monkey():

    def __init__(self, initial_items, operation, test, test_pass, test_fail):

        self.items = initial_items
        self.operation = operation
        self.modularity = test
        self.test_pass = test_pass
        self.test_fail = test_fail
        self.inspections = 0

    @staticmethod
    def _function_from_string(string):

        op_list = string.split(" ")
        operations = {"+": operator.add, "-": operator.sub, "*": operator.mul }
        n_old = sum([ 1 if i == "old" else 0 for i in op_list ])

        def function(x):

            if n_old == 1:

                return int(operations[op_list[1]](x, int(op_list[2])))
            
            elif n_old == 2:

                return int(operations[op_list[1]](x, x))
            
            else:

                raise TypeError("Unable to determine the monkey function")


        return function

    @classmethod
    def from_string(self, string_list):


        item_finder = re.compile("\d+")

        ## Defining the monkey items
        
        monkey_items = np.array(item_finder.findall(string_list[0]), dtype = int)
        
        items = [int(i) for i in monkey_items]

        ## Getting the monkey fuction
        ## All funtions are of the type a @ b, with a, b either the variable or a constant, and @ = *, +, -
        ## We use a method of the class to generate them

        op_str = string_list[1].replace("  Operation: new = ", "")
        operation = self._function_from_string(op_str)
        
        ## Defining the test

        test = int(item_finder.findall(string_list[2])[0])

        ## If pass

        test_pass = int(item_finder.findall(string_list[3])[0])

        ## If not pass

        test_fail = int(item_finder.findall(string_list[4])[0])

        return Monkey(items, operation, test, test_pass, test_fail)

    def inspect_one(self):

        item = self.items.pop(0)
        updated_item = np.floor(self.operation(item)/3)
        target = self.test_pass if updated_item%self.modularity == 0 else self.test_fail
        self.inspections += 1

        return updated_item, target

## Data Loading

with open("data_monkeys.dat", "r") as file:
    Lines = file.readlines()
for i, line in enumerate(Lines):
    Lines[i] = line.replace("\n", "")

monkey_strings = []

for i, line in enumerate(Lines):

    if line.startswith("Monkey"):
        monkey_strings.append(Lines[i+1:i+6])

## Initializing baboons

monkeys = [Monkey.from_string(s) for s in monkey_strings]

## Calculations for 20 rounds

for _ in range(20):

    for m in monkeys:
        for i in range(len(m.items)):

            item, target = m.inspect_one()
            monkeys[target].items.append(item)

activities = np.array([m.inspections for m in monkeys])
activities.sort()
monkey_business = activities[-1] * activities[-2]

print(f"After 20 rounds, the level of monkey business is {monkey_business}")



####################
#### PART 2 ########
####################


## We are going to encode the items into modular arithmetic. Each item will become a list
## The list will have an item for each monkey, and it will be of the form l = [N%t0, N%t1, ...] with ti the test number of the i-th monkey
## This way, each monkey only has to look at l[i] and check for a zero
## Monkey operations are carried out in modular arithmetic, which prevents the numbers from getting too large


## We need a new kind of monkey that understands modular arithmetic

class ModularMonkey():

    def __init__(self, initial_items, operation, test, test_pass, test_fail):

        self.starting_items = initial_items
        self.modular_items = None
        self.operation = operation
        self.modularity = test
        self.test_pass = test_pass
        self.test_fail = test_fail
        self.inspections = 0

    
    @staticmethod
    def _function_from_string(string, modularity):

        op_list = string.split(" ")
        operations = {"+": operator.add, "-": operator.sub, "*": operator.mul }
        n_old = sum([ 1 if i == "old" else 0 for i in op_list ])

        def function(x, modularity):

            if n_old == 1:

                return int(operations[op_list[1]](x, int(op_list[2])))%modularity
            
            elif n_old == 2:

                return int(operations[op_list[1]](x%modularity, x%modularity))
            
            else:

                raise TypeError("Unable to determine the monkey function")


        return function

    @classmethod
    def from_string(self, string_list):


        item_finder = re.compile("\d+")

        ## Defining the monkey items
        
        monkey_items = np.array(item_finder.findall(string_list[0]), dtype = int)
        
        items = [int(i) for i in monkey_items]

        ## Defining the test (modularity)

        test = int(item_finder.findall(string_list[2])[0])

        ## Getting the monkey fuction
        ## All funtions are of the type a @ b, with a, b either the variable or a constant, and @ = *, +, -
        ## We use a method of the class to generate them

        op_str = string_list[1].replace("  Operation: new = ", "")
        operation = self._function_from_string(op_str, test)
        
        ## If pass

        test_pass = int(item_finder.findall(string_list[3])[0])

        ## If not pass

        test_fail = int(item_finder.findall(string_list[4])[0])

        return ModularMonkey(items, operation, test, test_pass, test_fail)


## We also will need a class to manage a collection of modular monkeys

class ModularGroup():

    def __init__(self, monkey_group):

        self.monkeys = monkey_group
        self.modularities = [ m.modularity for m in monkey_group]

        for monkey in self.monkeys:

            monkey.modular_items = [ np.array([ item%mod for mod in self.modularities ]) for item in monkey.starting_items ]

    
    def inspect_one(self, monkey_index):

        item = self.monkeys[monkey_index].modular_items.pop(0)
        updated_item = np.array([ self.monkeys[monkey_index].operation(i, modularity)  for i, modularity in zip(item, self.modularities)])
        target = self.monkeys[monkey_index].test_pass if updated_item[monkey_index] == 0 else self.monkeys[monkey_index].test_fail
        self.monkeys[monkey_index].inspections += 1

        return updated_item, target
        

    def one_round(self):

        for i, m in enumerate(self.monkeys):
            for _ in range(len(m.modular_items)):
                item, target = self.inspect_one(i)
                self.monkeys[target].modular_items.append(item)


    def multiple_rounds(self, N):

        for _ in range(N):

            self.one_round()


monkeys = [ModularMonkey.from_string(s) for s in monkey_strings]

group = ModularGroup(monkeys)

group.multiple_rounds(10000)


activities = np.array([m.inspections for m in group.monkeys])
activities.sort()
monkey_business = activities[-1] * activities[-2]

print(f"After 10 000 rounds, the level of monkey business is {monkey_business}")