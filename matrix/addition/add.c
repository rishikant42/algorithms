#include <stdio.h>

int main() {
  int i = 0, j = 0;
  int a[2][2] = {1, 2, 3, 4};
  int b[2][2] = {5, 6, 7, 8};
  int c[2][2];

  int x[2][2],  y[2][2],  z[2][2];


  for(i=0; i<2; i++)
    for(j=0; j<2; j++) {
      printf("Enter element %d %d of first matrix: ", i, j);
      scanf("%d", &x[i][j]);
    }
  
  printf("\n");

  for(i=0; i<2; i++)
    for(j=0; j<2; j++) {
      printf("Enter element %d %d of second matrix: ", i, j);
      scanf("%d", &y[i][j]);
    }

  printf("\n");

  for(i=0; i<2; i++)
    for(j=0; j<2; j++)
      z[i][j] = x[i][j] +  y[i][j];

  printf("Resultant matrix: \n");

  for(i=0; i<2; i++)
    for(j=0; j<2; j++)
      printf("%d\n", z[i][j]);

//  for(i=0; i<2; i++)
//    for(j=0; j<2; j++)
//      c[i][j] = a[i][j] +  b[i][j];
//
//  for(i=0; i<2; i++)
//    for(j=0; j<2; j++)
//      printf("%d\n", c[i][j]);

  return 0;
}
