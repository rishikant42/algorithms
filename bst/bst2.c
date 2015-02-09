#include<stdio.h>
#include<stdlib.h>

typedef struct bsTree
{
int data;
struct bsTree *left;
struct bsTree *right;
}bsTree;

bsTree *Insert(bsTree *node,int data)
{
if(node == NULL)
{
bsTree *temp;
temp = (bsTree *)malloc(sizeof(bsTree));
temp->data = data;
temp->left = temp->right = NULL;
return temp;
}

else if(data > (node->data))
{
node->right = Insert(node->right,data);
return node;
}

else if(data < (node->data))
{
node->left = Insert(node->left,data);
return node;
}
return node;
}

void display1(bsTree *node)
{
if(node == NULL)
{
return;
}
else
{
display1(node->left);
printf("%d  ",node->data);
display1(node->right);
}

}

void display2(bsTree *node)
{
if(node == NULL)
{
return;
}
else
{
display2(node->left);
display2(node->right);
printf("%d  ",node->data);
}
}

void display3(bsTree *node)
{
if(node==NULL)
{
return;
}
printf("%d  ",node->data);
display3(node->left);
display3(node->right);
}

int main()
{
bsTree *root = NULL;
root = Insert(root,50);
root = Insert(root,44);
root = Insert(root,48);
root = Insert(root,75);
root = Insert(root,5);
root = Insert(root,80);
root = Insert(root,3);
root = Insert(root,11);
root = Insert(root,1);
root = Insert(root,77);

display1(root);                       //display1 method can be used for sorting
printf("\n");

display2(root);
printf("\n");

display3(root);
printf("\n");

return 0;
}
