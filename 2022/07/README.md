## DAY 7 -- NO SPACE LEFT ON DEVICE

During the journey through the jungle, I notice that my communication system is buggy. As a first reflex, I wanted to update that damn sytem but it pull out a daunting error `no space left on device`...

Hence the 1st quest of today: how can I make some space for the update?

After parsing the filesystem of the device, I end up with a history of the terminal ouput (ie. the input).
Based on this history I must compute the size of each folder and determine the total size of all folders with a size lower than 100,000. 

Knowing that the total dispace available to the filesystem is 70,000,000 and that I need at least 30,000,000 to update, I must find the smallest directory that when deleting would free up enough space on the filesystem. 

Hence the 2nd quest of the day: what is the total size of such folder?

### INPUT DESCRIPTION 

- each line is either a command line (begins with `$`) or an output (otherwise)
- the command `cd` is used to move through the filesystem 
    - `cd ..` moves out one level
    - `cd x` moves in the folder named `x`
    - `cd \` switches to the outmermost folder, aka the root. 
- the command `ls` lists all ouputs of the given folder
    - outputs can either be 
        - a folder when it begins with `dir` 
        - a file when it begins with a number which represents the size

### SOLVING METHOD

- Let's define 2 objects : 
    1. `File(name,size)`:
        - `self.name`: name of the file
        - `self.size`: size of the file
    2. `Folder(name,parent)`:
        - attributes: 
            - `self.name`: name of the folder
            - `self.parent`: name of the parent's folder (one level above -- closer to the `/`)
            - `self.files`: list of the file present at the level
            - `self.folders`: list of the folder present at this level
        - methods: 
            - `add_file(name,size)`: add a new file in this folder
            - `add_folder(name)`: add a new directory in this folder
            - `give_total_size()`: compute the sum of all files in this folder and in all sub-folder
- Set `actual_name_folder = "/"`  
- Recreate the root folder `/` by reading `input.txt` line by line
    - if line begins with `$ cd`:
        - if the command is `".."` set the `actual_name_folder` to the `Folder.parent`
        - else set the `actual_name_folder` to the name of the folder after `cd`
    - if line begins with `$ ls`
        - while line does not begins with `$`
            - split the line in two 
            - if the first is dir, create a new folder
            - else, create a new file
- compute the sum of all folders with a size lower than 100000
- compute which minimal folder needs to be deleting in order to free enough space of the disk
