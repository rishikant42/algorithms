#include<stdio.h>

#define MAX 10

void push(int num);
int pop();
void display();

int arr[MAX],top = -1;

int main()
{

push(1);
push(2);
push(3);
push(4);
push(5);

display();

printf("item popped = %d\n",pop());
printf("item popped = %d\n",pop());

display();

return 0;
}

void push(int num)
{
if(top == MAX-1)
	printf("stack is full\n");
top++;
arr[top] = num;
}

int pop()
{
if(top == -1)
	printf("stack is empty\n");

return arr[top--];
}

void display()
{
int i;
for(i=0;i<5;i++)
	printf("%d  ",arr[i]);
printf("\n");
}
