// each line is a rucksack with two compartiments
// each character is an item type with a priority set from a = 1 to Z = 52
// two compartiments contains same number of items
// 1st puzzle: for each line split in two equal length string and find the common character, and add to priorityScore
// 2st puzzle: for each group of 3 lines, find common character, and add to stickerScore
#include <stdio.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <stdlib.h>
#include <string.h>

double get_memory_used() {
    struct rusage r_usage;
    getrusage(RUSAGE_SELF, &r_usage);
    // Convert from KB to MB
    return r_usage.ru_maxrss / 1024.0;
}

#define MAX_LINES 301
#define MAX_LENGTH 128

int main() {
  struct timeval start, end;
  gettimeofday(&start, NULL);

  FILE *file = fopen("./input.txt", "r");
  if (file == NULL) {
    printf("Error opening file\n");
    return 1;
  }

  char sacks[MAX_LINES][MAX_LENGTH];
  int count = 0;

  while (count < MAX_LINES && fgets(sacks[count], MAX_LENGTH, file) != NULL) {
    count++;
  }
  fclose(file);

  for (int i = 0; i < count; i++){
    int size_compartement = strlen(sacks[i]);
    int mid = size_compartement/2;

    char* left_half = malloc(mid + 1);
    char* right_half = malloc(mid + 1);

    strncpy(left_half, &sacks[i][0], mid);
    left_half[mid] = '\0';

    strcpy(right_half, &sacks[i][mid]);

    printf("First half: %s\n", left_half);
    printf("Second half: %s\n", right_half);
  }
  gettimeofday(&end, NULL);
  double time_ms = (end.tv_sec - start.tv_sec) * 1000.0 +
                  (end.tv_usec - start.tv_usec) / 1000.0;
  
  double memory_mb = get_memory_used();
  
  printf("The script used approximately %.2f MB\n", memory_mb);
  printf("And it took approximately %.2f ms to run\n", time_ms);
  return 0;
}
