#include<stdio.h>
#include<stdlib.h>

#define MAX 10

int arr[MAX];
int rear;
int front;

void addq(int x);
int delq();
void display();

int main()
{
rear = -1;
front = -1;
addq(1);
addq(2);
addq(3);
addq(4);
addq(5);
printf("Item popped = %d\n",delq());
printf("Item popped = %d\n",delq());
display();
return 0;
}

void addq(int x)
{
if(rear == MAX-1)
	printf("queue is full\n");
//rear++;
arr[++rear] = x;

if(front == -1)
	front = 0;

}

int delq()
{
if(front == -1)
	printf("queue is empty\n");
int data = arr[front++];
//front++;

if(front == rear)
	front = rear = -1;
return data;
}

void display()
{
int i;
for(i=0;i<5;i++)
	printf("%d ",arr[i]);
printf("\n");
}
