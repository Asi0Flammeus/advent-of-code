## DAY 10 -- CATHODE-RAY TUBE

Okay due to this shitty rope-bridge, I was forced to jump into the river. 
Now I have to contact them with the communication system that the elves handed me few days ago.
But because the universe seems against me, my device has a big crack on the screen due to my fall. 

However I can figure out the signal being sent by the CPU based on instruction (ie. today's input).
The screen and CPU work in hand with a clock circuit. Each tick is a cycle.

The CPU is defined by a single register `X` which starts at 1. 
What would be the total sum of signal strength during each cycle 20 modulo 40 (20, 60, 100, etc..) ? 

The signal strength is simply define as the product between the register and the cycle number.

### INPUT 

- a txt file where each line is an instruction that begins by `addx Z` or `noop`:
    - `addx Z` means that you add the interger `Z` to `X` after two cycles
    - `noop` means that you pass to the next cycle
- after each line the number of cycle is incremented by one


### SOLVING METHOD 

- define `cycle_number = 1` and `X = 1` and `total_signal_strength = 0`
- define `pending_sum = [[0], [0], [0]]` which represents the pending value to be add to `X` 
    - `pending_sum[i]` is the value that would be add to X in i cycle. 
- read the input txt file line by line
    - add `pending_sum.pop(0)` to `X`
    - based on the instruction of the input 
        - if it's `addx Z` then append the integer `Z` to `pending_sum`
        - if it's `noop` then append 0 to `pending_sum`
    - if `cycle_number` is equal to 20 modulo 40
        - compute `signal_strength = cycle_number * X`
        - add `signal_strength` to `total_signal_strength`
    - add one to the `cycle_number`


