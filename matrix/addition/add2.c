#include <stdio.h>

int main() {
  int i = 0, j = 0, r, c;

  printf("\nEnter no of row: ");
  scanf("%d", &r);

  printf("\nEnter no of coloumn: ");
  scanf("%d", &c);

  int x[r][c],  y[r][c],  z[r][c];

  for(i=0; i<r; i++)
    for(j=0; j<r; j++) {
      printf("Enter element %d %d of first matrix: ", i+1, j+1);  
      scanf("%d", &x[i][j]);
    }
  
  //Array index initialization with 0, but matrix representation generally start with 1, so add 1 each time

  printf("\n");

  for(i=0; i<r; i++)
    for(j=0; j<r; j++) {
      printf("Enter element %d %d of second matrix: ", i+1, j+1);
      scanf("%d", &y[i][j]);
    }

  printf("\n");

  for(i=0; i<r; i++)
    for(j=0; j<r; j++)
      z[i][j] = x[i][j] +  y[i][j];

  printf("Resultant matrix: \n");

  for(i=0; i<r; i++)
    for(j=0; j<r; j++)
      printf("%d\n", z[i][j]);

  return 0;
}
