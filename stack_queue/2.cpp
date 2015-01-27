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

void addq(int num)
{
if(rear == MAX-1)
	cout<<"queue is full\n";

rear += 1;
arr[rear] = num;

if(front == -1)
	front = 0;
}

int delq()
{
if(rear == -1)
	cout<<"queue is empty\n";
int data = arr[front];
front += 1;

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
queue a;
a.addq(1);
a.addq(2);
a.addq(3);
a.addq(4);
a.addq(5);

a.display();

cout<<"Item deleted = "<<a.delq()<<endl;
cout<<"Item deleted = "<<a.delq()<<endl;

a.display();

return 0;
}

