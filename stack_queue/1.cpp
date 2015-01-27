#include<iostream>
using namespace std;

#define MAX 10

class stack
{
private:
int arr[10];
int top;

public:
stack()
{
top = -1;
}

void push(int num)
{
if(top == MAX-1)
{
cout<<"stack is full\n";
}
top++;
arr[top] = num;
}

int pop()
{
if(top == -1)
{
cout<<"stack is empty\n";
return 0;
}
int data = arr[top];
top--;
return data;
}

void display()
{
int i;				//instead of using 6 in for loop, we can calute size of arr
for(i=0;i<6;i++)		//size of array can be caluated by using sizeof() method which is declare in stdlib.h
	cout<<arr[i]<<" ";      //check rk.c
cout<<endl;
}

};


int main()
{
stack s;
s.push(1);
s.push(2);
s.push(3);
s.push(4);
s.push(5);
s.push(6);

s.display();

cout<<"item popped = "<<s.pop()<<"\n";
cout<<"item poped = "<<s.pop()<<"\n";

s.display();

return 0;
}

