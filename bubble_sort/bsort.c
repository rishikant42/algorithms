#include<stdio.h>

int main() {
  int a[8] = {8, 2, 6, 4, 3, 1, 7, 5};
  int i, j, k, tmp;

  for(i=0;i<8;i++) {
    for(j=0;j<8;j++) {
      if (j+1 < 8 && a[j] > a[j+1]) {
        tmp = a[j];
        a[j] = a[j+1];
        a[j+1] = tmp;

      }
    }
  }

  for(i=0;i<8;i++)
    printf("%d\n", a[i]);

  return 0;
}
