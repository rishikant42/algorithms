#include<iostream>
using namespace std;

#define MAX 10

class queue
{
int arr[MAX];
int rear,front;

public:
queue()
{
rear = -1;
front = -1;
}

void insert(int x)
{
if(rear == MAX-1)
	cout<<"queue is full\n";
rear++;
arr[rear] = x;

if(front == -1)
	front = 0;
}

int pop()
{
if(front == -1)
	cout<<"queue is empty\n";

int data = arr[front];
front++;

if(front == rear)
	front = rear = -1;
return data;
}

void display()
{
int i;
for(i=0;i<5;i++)
	cout<<arr[i]<<" ";
cout<<endl;
}

};

int main()
{
queue q;
q.insert(1);
q.insert(2);
q.insert(3);
q.insert(4);
q.insert(5);

cout<<"Item poppped = "<<q.pop()<<endl;
cout<<"Item popped = "<<q.pop()<<endl;

q.display();
return 0;
}
