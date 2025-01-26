// read each line
// define 4 constants, inf_left, sup_left, inf_right, sup_right
// define "fully contained"
// count number of fully contained line
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/resource.h>

double get_memory_used() {
    struct rusage r_usage;
    getrusage(RUSAGE_SELF, &r_usage);
    // Convert from KB to MB
    return r_usage.ru_maxrss / 1024.0;
}
#define MAX_LINES 1001
#define MAX_LENGTH 21


int main(){
  struct timeval start, end;
  gettimeofday(&start, NULL);

  FILE *file = fopen("./input.txt", "r");
  if (file == NULL){
    printf("Error opening file\n");
    return 1;
  }

  char assignment_ranges[MAX_LINES][MAX_LENGTH];
  int count = 0;
  int fullyContained = 0;
  int partillyContained = 0;

  while (count < MAX_LINES && fgets(assignment_ranges[count], MAX_LENGTH, file) != NULL) {
    /* printf("%s\n", assignment_ranges[count]); */
    char *parts[4];
    int inf_left;
    int sup_left;
    int inf_right;
    int sup_right;

    int i = 0;
    
    char *token = strtok(assignment_ranges[count], ",-");
    while (token != NULL && i < 4){
      parts[i++] = token;
      token = strtok(NULL, ",-");
    }

    /* for (int j = 0; j < 4; j++){ */
    /*   printf("%s\n", parts[j]); */
    /**/
    /* } */
    inf_left = atoi(parts[0]);
    sup_left = atoi(parts[1]);

    inf_right = atoi(parts[2]);
    sup_right = atoi(parts[3]);
    /* printf("%d\n", inf_left); */
    /* printf("%d\n", sup_left); */
    /* printf("%d\n", inf_right); */
    /* printf("%d\n", sup_right); */
    int distance_left = sup_left - inf_left;
    int distance_right = sup_right - inf_right;
    /* printf("%d\n", distance_left); */
    /* printf("%d\n", distance_right); */
    /* printf("\n"); */

    if (distance_left >= distance_right){
      if (inf_right >= inf_left && sup_right <= sup_left){
        fullyContained += 1;
      }
    }
    else if (distance_right >= distance_left){
      if (inf_left >= inf_right && sup_left <= sup_right){
        fullyContained += 1;
      }
    }

    if (inf_left >= inf_right && inf_left <= sup_right) {
      partillyContained += 1;
    }
    else if (sup_left >= inf_right && sup_left <= sup_right) {
      partillyContained += 1;
    }
    else if (inf_right >= inf_left && inf_right <= sup_left){
      partillyContained += 1;
    }
    else if (sup_right >= inf_left && sup_right <= sup_left) {
      partillyContained += 1;
    }
    /* printf("%d\n", fullyContained); */
    /* printf("========\n"); */
    count++;
  }
  fclose(file);
  
  printf("First Puzzle answer is: %d\n", fullyContained);
  printf("Second Puzzle answer is: %d\n", partillyContained);
  gettimeofday(&end, NULL);
  double time_ms = (end.tv_sec - start.tv_sec) * 1000.0 +
                  (end.tv_usec - start.tv_usec) / 1000.0;
  
  double memory_mb = get_memory_used();
  
  printf("The script used approximately %.2f MB\n", memory_mb);
  printf("And it took approximately %.2f ms to run\n", time_ms);
  return 0;
}
