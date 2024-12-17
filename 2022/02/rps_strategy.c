// read input.txt
// define an array based on the first column
// define another array based on the second column 
// for each round compute the output with a function evaluate_score
// A = Rock, B = Paper, C = Scissors
// 1st puzzle: X = R, Y = P, Z = S
// Score evaluation: 
// lost = 0, draw = 3, win = 6
// R = 1, P = 2, S = 3

#include <stdio.h> 
#include <stdlib.h>

#define MAX_LINES 2550

int main() {
  FILE *file = fopen("./input.txt", "r");
  if (file == NULL) {
    printf("Error opening file\n");
    return 1;
  }

  char otherStategy[MAX_LINES];
  char myStrategy[MAX_LINES];
  int count = 0;

  while (count < MAX_LINES && fscanf(file, " %c %c", &otherStategy[count], &myStrategy[count]) == 2) {
    count++;
  }

  fclose(file);

  for (int i = 0; i < count; i++) {
    printf("Line %d: %c %c\n", i, otherStategy[i], myStrategy[i]);
  }
  return 0;
}

