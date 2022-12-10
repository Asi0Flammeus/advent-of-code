import time
import psutil
import copy
from filesystem import File, Folder

start_time = time.time()

""" Recreate the root folder by reading input.txt line by line
"""
# Set the actual folder to the root
root_folder = Folder("/", None)
actual_folder = copy.deepcopy(root_folder)
actual_folder = root_folder
all_folders = []

with open("input.txt") as f:
    next(f)
    for line in f:
        if line.startswith("$ cd"):
            # Get the name of the folder to switch to
            name = line.split(" ")[-1].strip()
            if name == "..":
                # If the command is "..", set the actual_name_folder to the Folder.parent
                actual_folder = actual_folder.parent
            else:
                # Otherwise, set the actual_name_folder to the name of the folder after "cd"
                for folder in actual_folder.folders:
                    if folder.name == str(name):
                        actual_folder = folder
                        all_folders.append(folder)
        elif not line.startswith("$ ls"):
            # Split the line into two parts
            parts = line.split(" ")
            if parts[0] == "dir":
                # If the first part is "dir", create a new folder
                name = parts[1].strip()
                actual_folder.add_folder(name)
            else:
                # Otherwise, create a new file
                name = parts[1]
                size = int(parts[0])
                actual_folder.add_file(name,size)

""" Compute the sum of all root folders with a size lower than 100000
    and also the candidate folder size for allowing the update
"""
total_size = 0
DISK_SPACE = 70000000
NEEDED_SPACE = 30000000
DISK_SPACE_USED = root_folder.give_total_size()
candidate_folder_size = root_folder.give_total_size()

for folder in all_folders:
    # first part of the puzzle
    if folder.give_total_size() < 100000:
        total_size += folder.give_total_size()
    # second part of the puzzle
    if DISK_SPACE - (DISK_SPACE_USED - folder.give_total_size()) > NEEDED_SPACE:
        candidate_folder_size = min(candidate_folder_size,folder.give_total_size())

""" pull out answers and script performance
"""
print("the first answer is",total_size)
print("the second answer is",candidate_folder_size)

# calculate the memory usage
used = psutil.Process().memory_info().rss / 1024 / 1024
# print the memory usage, rounded to two decimal places
print()
print(f"The script used approximately {round(used * 100) / 100} MB")

# calculate the elapsed time
elapsed_time = time.time() - start_time
# print the elapsed time, rounded to two decimal places
print(f"And it took approximately {round(elapsed_time*1000, 2)} ms to run")

