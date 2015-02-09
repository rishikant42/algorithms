#include<stdio.h>
void max_heap(int a[10],int i);
void build_max(int a[10]);

void main()
{

int p[10] = {1,14,10,8,7,9,3,2,4,6};
build_max(p);
}

void max_heap(int a[10],int i)
{
int l,r,s,largest;

    l = 2*i + 1;
    r = 2*i + 2;
    s = 10;

    if(l<s && a[l] >= a[i])
        largest = l;
    else
      largest = i;

    if(r<s && a[r] >= a[largest])
       largest = r;

    if(a[i] != a[largest])
{
int t;
        t = a[i];
        a[i] = a[largest];
        a[largest] = t;


for(i=0;i<10;i++)
printf("%d ",a[i]);
printf("\n");

max_heap(a,largest);

}

}

void build_max(int a[10])
{
int i;
for(i=5;i>=0;i++)
max_heap(a,i);
}
