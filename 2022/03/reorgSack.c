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
#include <stdbool.h>

double get_memory_used() {
    struct rusage r_usage;
    getrusage(RUSAGE_SELF, &r_usage);
    // Convert from KB to MB
    return r_usage.ru_maxrss / 1024.0;
}

#define MAX_LINES 1000
#define MAX_LENGTH 128

int getPriorityScore(const char *left, const char *right) {
  int priorityScore = 0;
  int letterExist[52] = {0}; // 26 lower and 26 uppercase letters

  int getIndex(char c) {
    if (c >= 'a')
      return c - 'a';
    return c - 'A' + 26;
  }
  for (int i = 0; left[i]; i++) {
    int index = getIndex(left[i]);
    letterExist[getIndex(left[i])] = 1;
  }

  // replace with a whiles:
  bool foundCommon = false;
  int i = 0; 
  while (!foundCommon && right[i] != '\0') {
    int index = getIndex(right[i]);
    if (letterExist[index] == 1) {
      /* printf("%c\n", right[i]); */
      priorityScore += index + 1;
      foundCommon = true;
    }
    i += 1;
  }
  return priorityScore;
}

int getStickerScore(const char *first, const char *second, const char *third) {
  int stickerScore = 0;
  int letterExist[52] = {0}; // 26 lower and 26 uppercase letters

  int getIndex(char c) {
    if (c >= 'a')
      return c - 'a';
    return c - 'A' + 26;
  }
  for (int i = 0; first[i]; i++) {
    int index = getIndex(first[i]);
    letterExist[getIndex(first[i])] = 1;
  }
  for (int i = 0; second[i]; i++) {
    int index = getIndex(second[i]);
    if (letterExist[index] == 1) {
      letterExist[getIndex(second[i])] = 2;
    }
  }

  for (int i = 0; i < 52; i++){
    printf("%d ", letterExist[i]);
  }
  printf("\n");
  bool foundCommon = false;
  int i = 0; 
  while (!foundCommon && third[i] != '\0') {
    int index = getIndex(third[i]);
    if (letterExist[index] == 2) {
      printf("%d\n", index);
      printf("%c\n", third[i]);
      stickerScore += index + 1;
      foundCommon = true;
    }
    i += 1;
  }
  return stickerScore;
}

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
  int priorityScore = 0;
  int stickerScore = 0;
  while (count < MAX_LINES && fgets(sacks[count], MAX_LENGTH, file) != NULL) {
    count++;
  }
  fclose(file);

  for (int i = 0; i < count; i += 3){
    for (int j = 0; j < 3; j++) {
      int idx = i + j;
      int size_compartement = strlen(sacks[idx]);
      int mid = size_compartement/2;

      char* left_half = malloc(mid + 1);
      char* right_half = malloc(mid + 1);

      strncpy(left_half, &sacks[idx][0], mid);
      left_half[mid] = '\0';
      strcpy(right_half, &sacks[idx][mid]);

      priorityScore += getPriorityScore(left_half, right_half);

    /* printf("index: %d\n", idx); */
    }
    stickerScore += getStickerScore(sacks[i], sacks[i+1], sacks[i+2]);
    printf("stickerScore: %d\n", stickerScore);
    printf("\n");
  }

  printf("Priority Score is: %d\n", priorityScore);
  printf("Sticker Score is: %d\n", stickerScore);

  gettimeofday(&end, NULL);
  double time_ms = (end.tv_sec - start.tv_sec) * 1000.0 +
                  (end.tv_usec - start.tv_usec) / 1000.0;
  
  double memory_mb = get_memory_used();
  
  printf("The script used approximately %.2f MB\n", memory_mb);
  printf("And it took approximately %.2f ms to run\n", time_ms);
  return 0;
}
