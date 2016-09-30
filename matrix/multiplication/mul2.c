#include <stdio.h>
#include <stdlib.h>

int main() {
  int i, j, k, r1, c1, r2, c2;

  printf("\nEnter no of row in first matrix: ");
  scanf("%d", &r1);
  
  printf("\nEnter no of column in first matrix: ");
  scanf("%d", &c1);

  printf("\nEnter no of row in second matrix: ");
  scanf("%d", &r2);
  
  printf("\nEnter no of column in second matrix: ");
  scanf("%d", &c2);

  int a[r1][c1], b[r2][c2], c[r1][c2]; 

  if(c1 != r2)
    printf("\nERROR: Matrix multiplication is not possible\n");

  else {
    for(i=0; i<r1; i++)
      for(j=0; j<c1; j++) {
        printf("\nEnter %d %d element of first matrix: ", i+1, j+1);
        scanf("%d", &a[i][j]);
      }

    for(i=0; i<r2; i++)
      for(j=0; j<c2; j++) {
        printf("\nEnter %d %d element of second matrix: ", i+1, j+1);
        scanf("%d", &b[i][j]);
      }



    for(i=0; i<r1; i++)
      for(j=0; j<c2; j++) {
        c[i][j] = 0;
        for(k=0; k<r2; k++)
          c[i][j] += a[i][k] * b[k][j];
      }

    printf("\nResultant Matrix: \n");

    for(i=0; i<r1; i++)
      for(j=0; j<c2; j++) 
        printf("%d\n", c[i][j]);
  }


  return 0;
}
