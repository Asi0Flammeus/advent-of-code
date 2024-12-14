#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/time.h>
#include <sys/resource.h>
#include "../../libs/algorithms.h"

double get_memory_used() {
    struct rusage r_usage;
    getrusage(RUSAGE_SELF, &r_usage);
    // Convert from KB to MB
    return r_usage.ru_maxrss / 1024.0;
}

int main() { 
  struct timeval start, end;
  gettimeofday(&start, NULL);

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

    if (isEmpty && INVENTORY_CALORY > 0) {
      /* printf("inventory total calorie: %d\n", inventories_p[INVENTORY_SIZE-1]); */
      INVENTORY_SIZE ++; 
      inventories_p = realloc(inventories_p, INVENTORY_SIZE * sizeof(int));
      inventories_p[INVENTORY_SIZE-1] = INVENTORY_CALORY;
      INVENTORY_CALORY = 0;
    } else if (sscanf(line, "%d", &value) == 1) {
      INVENTORY_CALORY += value;
    } else {
      /* printf("This line contains something else than an interger\n"); */
    }

  }

  fclose(file);

  quickSort(inventories_p, 0, INVENTORY_SIZE - 1);
  printf("(1) Highest calorie inventory: %d\n", inventories_p[INVENTORY_SIZE-1]);
  
  int TOP_THREE = inventories_p[INVENTORY_SIZE-1] + inventories_p[INVENTORY_SIZE-2] + inventories_p[INVENTORY_SIZE-3];
  printf("(2) Sum of top 3 is: %d\n", TOP_THREE);
  free(inventories_p);

  gettimeofday(&end, NULL);
  double time_ms = (end.tv_sec - start.tv_sec) * 1000.0 +
                  (end.tv_usec - start.tv_usec) / 1000.0;
  
  double memory_mb = get_memory_used();
  
  printf("The script used approximately %.2f MB\n", memory_mb);
  printf("And it took approximately %.2f ms to run\n", time_ms);

  return 0;
}

