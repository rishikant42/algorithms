#include<stdio.h>
#include<stdlib.h>

#define MAX 10

int arr[MAX];
int top = -1;

void push(int x);
int pop();
void display();

int main()
{
push(1);
push(2);
push(3);
push(4);
push(5);

printf("Item popped = %d\n",pop());
printf("Item popped = %d\n",pop());

display();

return 0;
}

void push(int x)
{
if(top == MAX-1)
	printf("stack is full\n");
top++;
arr[top] = x;
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
	printf("%d ",arr[i]);
printf("\n");
}
