#include<stdio.h>
#include<stdlib.h>

typedef struct avlTree
{
int data;
struct avlTree *left;
struct avlTree *right;
int height;
}avl;

int max(int a,int b)
{
return a>b?a:b;
}

int height(avl *N)
{
if(N == NULL)
return 0;

return N->height;
}

int getBalnce(avl *N)
{
if(N == NULL)
return;
return height(N->left) - height(N->right);
}


avl *rightRotate(avl *y)
{
avl *x = y->left;
avl *T2 = x->right;

x->right = y;
y->left = T2;

y->height = max(height(y->left),height(y->right))+1;
x->height = max(height(x->left),height(x->right))+1;

return x;
}

avl *leftRotate(avl *y)
{
avl *x = y->right;
avl *T2 = x->left;

x->left = y;
y->right = T2;

y->height = max(height(y->left),height(y->right))+1;
x->height = max(height(x->left),height(x->right))+1;

return x;
}

avl *Insert(avl *node,int val)
{
if(node == NULL)
{
avl *temp;
temp = (avl *)malloc(sizeof(avl));
temp->data = val;
temp->left = temp->right = NULL;
temp->height = 1;
return temp;
}

else if(val < (node->data))
{
node->left = Insert(node->left,val);
}

else
{
node->right = Insert(node->right,val);
}

node->height = max(height(node->left), height(node->right)) + 1;

int balance = getBalnce(node);

if(balance > 1 && val < node->left->data)
return rightRotate(node);

if(balance > 1 && val > node->left->data)
{
node->left = leftRotate(node->left);
return rightRotate(node);
}

if(balance < -1 && val > node->right->data)
return leftRotate(node);

if(balance < -1 && val < node->right->data)
{
node->right = rightRotate(node->right);
return leftRotate(node);
}

return node;
}


void display(avl *node)
{
if(node == NULL)
return;
else
{
printf("%d  ",node->data);
display(node->left);
display(node->right);
}
}

int main()
{
avl *root = NULL;
root = Insert(root,10);
root = Insert(root,20);
root = Insert(root,30);
root = Insert(root,40);
root = Insert(root,50);
root = Insert(root,25);
display(root);
printf("\n");
return 0;
}

