with open('input.txt', 'r') as file:
  # read the entire contents of the file into a string variable
  data = file.read()

# initialize the position to -1
pos = -1

# set the Start-of-Packet and Start-of-Message length
SoP_length = 4
SoM_length = 14


""" parse the data to find the position of the SoP length
"""
# loop through the characters in the data string
for i in range(len(data) - SoP_length - 1):
  # check if the current group of SoP_length characters are all different
  if len(set(data[i:i+SoP_length])) == SoP_length:
    # if they are, update the position and break out of the loop
    SoP_position = i + SoP_length
    break

# print the final position of the SoP
print("The answer is",SoP_position)

""" parse the data to find the position of the SoM length
"""
# loop through the characters in the data string
for i in range(len(data) - SoM_length - 1):
  # check if the current group of SoM_length characters are all different
  if len(set(data[i:i+SoM_length])) == SoM_length:
    # if they are, update the position and break out of the loop
    SoM_position = i + SoM_length
    break

# print the final position of the SoM 
print("The answer is",SoM_position)
