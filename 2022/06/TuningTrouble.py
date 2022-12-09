import psutil
import time
start_time = time.time()

def get_marker_position(data,length):
    """ parse the data to find the position of the marker
        of a given length
    """
    # initialize the position to -1
    position = -1

    # loop through the characters in the data string
    for i in range(len(data) - length - 1):
      # check if the current group of characters are all different
      if len(set(data[i:i+length])) == length:
        # if they are, update the position and break out of the loop
        position = i + length
        break
    return position

with open('input.txt', 'r') as file:
  # read the entire contents of the file into a string variable
  data = file.read()

# set the Start-of-Packet and Start-of-Message length
SoP_length = 4
SoM_length = 14

""" pull out answers and process performance
"""
# print the final position of the SoP
print("The 1st answer is",get_marker_position(data,SoP_length))
# print the final position of the SoM 
print("The 2nd answer is",get_marker_position(data,SoM_length))

# calculate the memory usage
used = psutil.Process().memory_info().rss / 1024 / 1024
# print the memory usage, rounded to two decimal places
print()
print(f"The script used approximately {round(used * 100) / 100} MB")

# calculate the elapsed time
elapsed_time = time.time() - start_time
# print the elapsed time, rounded to two decimal places
print(f"And it took approximately {round(elapsed_time*1000, 2)} ms to run")
