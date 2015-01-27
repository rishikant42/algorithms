#include<stdio.h>

#define MAX 10

void addq(int num);
int delq();
void display();

int arr[MAX];
int rear = -1;
int front = -1;

int main()
{
//rear = -1;		this approach is also possible.
//front = -1;		these value can be declare in main function
addq(1);
addq(2);
addq(3);
addq(4);
addq(5);

display();

printf("Item deleted = %d\n",delq());
printf("Item deleted = %d\n",delq());

display();

printf("%d  %d\n",rear,front);
return 0;
}

void addq(int num)
{
if(rear == MAX-1)
	printf("queue is fulled\n");
rear += 1;
arr[rear] = num;

if(front == -1)
	front = 0;
}

int delq()
{
if(rear == -1)
	printf("queue is empty\n");

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
	printf("%d ",arr[i]);
printf("\n");
}
