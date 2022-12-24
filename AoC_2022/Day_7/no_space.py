import numpy as np


class FileNavigator():

    def __init__(self):

        self.current_directory = []
        self.directories = {}

    def ls(self, *contents):

        if self.current_directory == ["/"]:
            string_directory = "/".join([_ for _ in self.current_directory])
        else:
            string_directory = "/".join([_ for _ in self.current_directory])[1:]

        if string_directory not in self.directories:

            dum = [item for item in contents]
            self.directories[string_directory] = dum

    def cd(self, path):
        
        if path == "..":
            self.current_directory.pop(-1)
        else:
            self.current_directory.append(path)

    def directory_size(self, key):

        path = key
        contents = self.directories[key]

        size = 0

        for item in contents:

            if type(item) == tuple:

                size += item[1]
            
            elif type(item) == str:
                if key == "/":
                    new_key = path + item
                else:
                    new_key = path + f"/{item}"
                size += self.directory_size(new_key)
            
        return size


with open('data_no_space.dat', 'r') as file:
    console_log = file.readlines()

for i, line in enumerate(console_log):
    console_log[i] = line.replace("\n", "")


console_log = np.array(console_log)

is_command = np.array([ line[0] == "$" for line in console_log])


user = FileNavigator()
for i, (line, iscommand) in enumerate(zip(console_log, is_command)):

    if iscommand:

        try:
            command, arg= line.strip("$ ").split(" ")
        except:
            command = line.strip("$ ").split(" ")[0]

        if command == "cd":

            user.cd(arg)

        elif command == "ls":

            try:
                stop = np.where(is_command[i+1:] == True )[0][0] 
                stop += i + 1
                ls_output = console_log[i+1:stop]

            except:
                ls_output = console_log[i+1:]


            treated_output = []

            for output in ls_output:

                id, name = output.split(" ")

                if id == "dir":
                    treated_output.append(name)
                else:
                    size = int(id)
                    treated_output.append((name, size))
            user.ls(*treated_output)

        else:
            raise ValueError(f"Invalid command found: {command}")



S = 0

for dir in user.directories:

    size = user.directory_size(dir)

    if size <= 100000:
        S += size

print(f"The total size into directories of size of at most 1e5 is {S}")



################################
################################
################################

total_space = 70000000

needed_space = 30000000

current_space = total_space - user.directory_size("/")

space_to_free = needed_space - current_space


size_deleted = total_space

for dir in user.directories:

    size = user.directory_size(dir)

    if size >= space_to_free:
        if size < size_deleted:
            size_deleted = size

print(f"The size of the smallest directory that can be deleted is {size_deleted}")