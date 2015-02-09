#include<iostream>
using namespace std;

int main()
{
int a[6] = {8,2,7,9,3,6};
int i,j,key;
for(j=1;j<6;j++)
{
key = a[j];
i = j-1;
while(i>=0 && a[i]>key)
{
a[i+1] = a[i];
i = i-1;
}
a[i+1] = key;
}

for(i=0;i<6;i++)
cout<<a[i]<<" ";

cout<<"\n";
return 0;
}
