## DAY 1 -- CALORIE COUNTING

The adventure begins! 
Each elf carries various food stuff in their inventory.
They need to know:
1. the elve with the most calories in its inventory
2. the sum of the top 3 of calories holder

### INPUT

- each line gives the calorie of one item 
- each elve inventory is spaced with a breakline

### SOLVING METHOD

- parse the input txt with `read` 
- for each elve create a list (the inventory) for all food stuff 
    - sum the calories of the sum and save it in an maximum_calories array
- if line is a linebreak (\n) then pass to the next inventory

