#include <stdio.h>

int main() {
  int i = 0, j = 0;
  int a[2][2] = {1, 2, 3, 4};
  int b[2][2] = {5, 6, 7, 8};

  printf("Resultant matrix: \n");

  for(i=0; i<2; i++)
    for(j=0; j<2; j++)
      printf("%d\n", a[i][j] + b[i][j]);

  return 0;
}
