## DAY 1 -- CALORIE COUNTING

The adventure begins!
Each elf carries various food stuff in their inventory.
They need to know:

1. the elve with the most calories in its inventory
2. the sum of the top 3 of calories holder

### INPUT

- a txt file where
  - each line gives the calorie of one item if line contains an `int`
  - each elve inventory is spaced with a breakline

### Expected Results

1. output the total colorie of the biggest inventory
2. output the sum of the 3 most biggest inventory total calorie

---

### Python Logs

- parse the input txt with `read`
- for each elve create a list (the inventory) for all food stuff
  - sum the calories of the sum and save it in an maximum_calories array
- if line is a linebreak (\n) then pass to the next inventory

### C logs

- inital strategy
  - [x] open the file
    - [ ] make it a function
  - [x] check if empty line or extract calorie value
  - [x] allocate dynamically memory for an array of total calorie
    - each element is the sum of food calorie they have in their inventory
  - [ ] sort the array
    - here would be the rabbit hole of sorting-algorithms
  - [ ] sum the top 3
  - [ ] find a way to estimate the RAM used for the script
  - [ ] find a way to estimate the run time of the script
