#include<stdio.h>

int main()
{
int a[5] = {5,3,4,2,1};
int b[5] = {};
int c[4] = {};
int i,j;
for(i=0;i<4;i++)
c[i] = 0;

for(j=0;j<5;j++)
c[a[j]] = c[a[j]] + 1;

for(i=1;i<4;i++)
c[i] = c[i] + c[i-1];

for(j=4;j>=0;j--)
{
b[c[a[j]]] = a[j];
c[a[j]] = c[a[j]]-1;
}

for(i=0;i<5;i++)
printf("%d  ",b[i]);

printf("\n");

return 0;
}


//sorting in linear time
//some error in programe
