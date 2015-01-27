#include<iostream>
using namespace std;

#define MAX 10

class stack
{
int arr[MAX];
int top;

public:
stack()
{
top = -1;
}

void push(int x)
{
if(top == MAX-1)
	cout<<"stack is full\n";
top++;
arr[top] = x;
}

int pop()
{
if(top == -1)
	cout<<"stack is empaty\n";

return arr[top--];
}

void display();
};

void stack::display()
{
int i;
for(i=0;i<5;i++)
	cout<<arr[i];
cout<<endl;
}

int main()
{
stack s;
s.push(1);
s.push(2);
s.push(3);
s.push(4);
s.push(5);
cout<<"Item popped = "<<s.pop()<<endl;
cout<<"Item popped = "<<s.pop()<<endl;
s.display();
return 0;
}
