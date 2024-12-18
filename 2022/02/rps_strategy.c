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
#include <sys/time.h>
#include <sys/resource.h>

double get_memory_used() {
    struct rusage r_usage;
    getrusage(RUSAGE_SELF, &r_usage);
    // Convert from KB to MB
    return r_usage.ru_maxrss / 1024.0;
}

#define MAX_LINES 2550

int main() {
  struct timeval start, end;
  gettimeofday(&start, NULL);

  FILE *file = fopen("./input.txt", "r");
  if (file == NULL) {
    printf("Error opening file\n");
    return 1;
  }

  char otherStrategy[MAX_LINES];
  char myStrategy[MAX_LINES];
  int count = 0;

  while (count < MAX_LINES && fscanf(file, " %c %c", &otherStrategy[count], &myStrategy[count]) == 2) {
    count++;
  }

  fclose(file);

  int rounds = count;
  int score = 0;
  int final_score = 0;
  for (int i = 0; i < rounds; i++) {
    /* printf("Line %d: %c %c\n", i, otherStrategy[i], myStrategy[i]); */
    if (myStrategy[i] == 'X'){
      score = score + 1;
      if (otherStrategy[i] == 'A'){
        score = score + 3;
      }
      else if (otherStrategy[i] == 'C'){
        score = score + 6;
      }
    }
    else if (myStrategy[i] == 'Y'){
      score = score + 2;
      if (otherStrategy[i] == 'A'){
        score = score + 6;
      }
      else if (otherStrategy[i] == 'B'){
        score = score + 3;
      }
    }
    else if (myStrategy[i] == 'Z'){
      score = score + 3;
      if (otherStrategy[i] == 'C'){
        score = score + 3;
      }
      else if (otherStrategy[i] == 'B'){
        score = score + 6;
      }
    }

    if (otherStrategy[i] == 'A'){
      if (myStrategy[i] == 'X'){
        final_score = final_score + 3 + 0;
      }
      if (myStrategy[i] == 'Y'){
        final_score = final_score + 1 + 3;
      }
      if (myStrategy[i] == 'Z'){
        final_score = final_score + 2 + 6;
      }
    }
    if (otherStrategy[i] == 'B'){
      if (myStrategy[i] == 'X'){
        final_score = final_score + 1 + 0;
      }
      if (myStrategy[i] == 'Y'){
        final_score = final_score + 2 + 3;
      }
      if (myStrategy[i] == 'Z'){
        final_score = final_score + 3 + 6;
      }
    }
    if (otherStrategy[i] == 'C'){
      if (myStrategy[i] == 'X'){
        final_score = final_score + 2 + 0;
      }
      if (myStrategy[i] == 'Y'){
        final_score = final_score + 3 + 3;
      }
      if (myStrategy[i] == 'Z'){
        final_score = final_score + 1 + 6;
      }
    }
  }
  printf("Score is: %d\n", score);
  printf("Score is: %d\n", final_score);

  gettimeofday(&end, NULL);
  double time_ms = (end.tv_sec - start.tv_sec) * 1000.0 +
                  (end.tv_usec - start.tv_usec) / 1000.0;
  
  double memory_mb = get_memory_used();
  
  printf("The script used approximately %.2f MB\n", memory_mb);
  printf("And it took approximately %.2f ms to run\n", time_ms);
  return 0;
}

