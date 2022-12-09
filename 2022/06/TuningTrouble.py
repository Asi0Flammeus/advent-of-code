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

# print the final position of the SoP
print("The 1st answer is",get_marker_position(data,SoP_length))
# print the final position of the SoM 
print("The 2nd answer is",get_marker_position(data,SoM_length))

