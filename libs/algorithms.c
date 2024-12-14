#include "algorithms.h"
#include <stdio.h>

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

static int get_pivot(int *arr, int low, int high) {
  /**
   * Get the pivot of an array
   * based on the median of three method
   */

  int mid = (low + high) / 2;

  if (arr[low] > arr[mid]) {
    swap(&arr[low], &arr[mid]);
  }
  if (arr[low] > arr[high]) {
    swap(&arr[low], &arr[high]);
  }
  if (arr[mid] > arr[high]) {
    swap(&arr[mid], &arr[high]);
  }
  return arr[mid];
}

static int hoare_partition(int *arr, int low, int high) {
  int pivot = get_pivot(arr, low, high);
  int i = low - 1;
  int j = high + 1;

  while (1){
    do {
      i++;
    } while (arr[i] < pivot);

    do {
      j--;
    } while (arr[j] > pivot);
  
    if (i >= j)
      return j;

    swap(&arr[i], &arr[j]);
  }
}
  
void quickSort(int *arr, int low, int high) {
  if (low < high) {
    int partition_index = hoare_partition(arr, low, high);

    quickSort(arr, low, partition_index);
    quickSort(arr, partition_index + 1, high);

  }
}

