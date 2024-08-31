#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main() { 
  FILE *file;
  char line[256];
  int value;

  file = fopen("./input.txt", "r");
  if (file == NULL) {
    printf("Could not open file\n");
    return 1;
  }

  while (fgets(line, sizeof(line), file)) {
    // Remove the newline character at the end of the line
    line[strcspn(line, "\n")] = 0;

    int isEmpty = 1;

    // check if empty line
    for (int i = 0; i < strlen(line); i++) {
      if (!isspace(line[i])) {
        isEmpty = 0;
        break;
      } 
    }

    if (isEmpty) {
      printf("The line is empty.\n");
    } else if (sscanf(line, "%d", &value) == 1) {
      printf("This inventory has a food of a calorie: %d\n", value);
    } else {
      printf("This line contains something else than an interger\n");
    }

  }

  fclose(file);
}

