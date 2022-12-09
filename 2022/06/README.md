## DAY 6 -- TUNING TROUBLE 

We are now our way to the star fruit grove. 
The elves an encrypted communication system and of course they give me a malfunctionning device. 
Therefore I need to repair it. 

Given a datastream buffer (ie. the input) of a seemingly random letters, I need to find a start-of-packet (SoP) marker. 
This SoP marker is defined as the first occurence of a group of 4 characters that are all different. 

My first goal is to write a subroutine that find the position of the last caracter of the SoP marker.

For instance, the position would be 7 with the following datastream buffer `mjqjpqmgbljsphdztnvjfqwrcgsmlb`.

The second goal is identical except that now I have to find the position of the Start-of-Message (SoM) marker which is defined as the SoP marker but for a length of 14 characters.

### SOLVING METHOD

- read the input txt file
- define the SoP and SoM length
- for each group of $N$ caracters check if the set length is equal to $N$
- if so then pull out the position of the marker
