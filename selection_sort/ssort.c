#include<stdio.h>
#include<stdlib.h>

int main()
{
  int i, j, least, swap;

  int a[10] = {8, 2, 6, 7, 10, 4, 3, 1, 5, 9};

  int size = sizeof(a) / sizeof(int);

  for (i = 0; i < size  ; i++)
  {
    least = i;

    for (j = i + 1; j < size ; j++)
    {
      if (a[j] < a[least] )
        least = j;


      if (least != i)
      {
        swap = a[i];
        a[i] = a[least];
        a[least] = swap;
      }

    }

  }

  printf("Sorted list in ascending order:\n");

  for (i = 0 ; i < size ; i++ )
    printf("%d\n", a[i]);

  return 0;
}
