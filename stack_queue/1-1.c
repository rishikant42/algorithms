#include<stdio.h>
#include<stdlib.h>

int main()
{
int i, a[10] = {1,2,3,4,5};
unsigned int k = sizeof(a)/4;
for(i=0;i<k;i++)
printf("%d\n",a[i]);
return 0;
}
