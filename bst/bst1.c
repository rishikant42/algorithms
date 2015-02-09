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

void display(bsTree *node)
{
if(node == NULL)
{
return;
}
else
{
display(node->left);
printf("%d  ",node->data);
display(node->right);
}

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

display(root);
printf("\n");

return 0;
}
