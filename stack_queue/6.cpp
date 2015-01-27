#include<iostream>
#include<stdlib.h>
using namespace std;

struct file
{
int data;
struct file *next;
};

class stack
{
struct file *top,*head1,*head2;

public:
stack()
{
top = NULL;
head1 = NULL;
head2 = NULL;
}

void push(int x)
{
struct file *temp;
temp = new file;
temp->data = x;
temp->next = top;
top = temp;
head1 = top;
head2 = head1;
}

int pop()
{
if(top == NULL)
{
	cout<<"stack is empty\n";
	return 0;
}

struct file *temp;
temp = top;
int item = temp->data;
top = top->next;
delete temp;
return item;
}
void display1()
{
while(head1 != NULL)
{
cout<< head1->data <<" ";
head1 = head1->next;
}
cout<<endl;
}

void display2()
{
while(head2 != NULL)
{
cout<< head2->data <<" ";
head2 = head2->next;
}
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
s.display1();
cout<<"Item popped = "<<s.pop()<<endl;
cout<<"Item popped = "<<s.pop()<<endl;
s.display2();
return 0;
}



