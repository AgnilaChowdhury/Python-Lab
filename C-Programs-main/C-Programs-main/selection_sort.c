#include <stdio.h>


void selectionSort(int *arr,int n) {
    int i, j, minIndex, temp;
 
     for (i = 0; i < n - 1; i++) {
        minIndex = i;

        // Find the index of the minimum element in the unsorted part of the array
        for (j = i + 1; j < n; j++) {
            if (*(arr + j) < *(arr + minIndex)) {
                minIndex = j;
            }
        }

        // Swap the found minimum element with the first element
        temp = *(arr + minIndex);
        *(arr + minIndex) = *(arr + i);
        *(arr + i) = temp;
    }
}


void printArray(int *arr,int size) {
    int i;
    
    for (i = 0; i < size; i++)
        printf("%d ",*(arr+i));
    printf("\n");
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
    printArray(arr,n);

   
    selectionSort(arr,n);

    printf("Sorted array: ");
    printArray(arr,n);

    return 0;
}
