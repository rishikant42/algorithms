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
struct file *top;

public:

stack()
{
top = NULL;
}

void push(int x)
{
struct file *temp;
temp = new file;
temp->data = x;
temp->next = top;       //must understand wts going on here
top = temp;		//top value change every time
}			//it is not same as insertion at begging in linked list bcoz there head is declare outside the main fn
			//it is something like prblm occuring in 1.cpp in ll directory
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
void display()
{
while(top != NULL)
{
cout<< top->data <<" ";
top = top->next;
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
//s.display();
cout<<"Item popped = "<<s.pop()<<endl;
cout<<"Item popped = "<<s.pop()<<endl;
s.display();
return 0;
}


//to performe 2 times display opertion we should make two pointer & two operation
