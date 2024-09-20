#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main() { 
  FILE *file;
  char line[256];
  int value;
  int INVENTORY_SIZE = 1;
  int INVENTORY_CALORY = 0;
  int* inventories_p = (int*)malloc(INVENTORY_SIZE * sizeof(int));


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
      inventories_p[INVENTORY_SIZE-1] = INVENTORY_CALORY;
      printf("inventory total calorie: %d\n", inventories_p[INVENTORY_SIZE-1]);
      INVENTORY_SIZE ++; 
      inventories_p = realloc(inventories_p, INVENTORY_SIZE * sizeof(int));
      INVENTORY_CALORY = 0;
    } else if (sscanf(line, "%d", &value) == 1) {
      INVENTORY_CALORY += value;
    } else {
      printf("This line contains something else than an interger\n");
    }

  }

  fclose(file);
  printf("number of elve's inventory: %d\n", INVENTORY_SIZE);
}

