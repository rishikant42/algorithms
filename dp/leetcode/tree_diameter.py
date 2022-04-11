class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def height(root, ans):
    if root == None:
        return 0

    left = height(root.left, ans)
    right = height(root.right, ans)


    # ans[0] = max(ans[0], left+right+1)

    # return 1 + max(left, right)
    temp = max(left, right) + 1
    ans[0] = max(temp, 1+left+right)
    return temp


def diameter(root):
    ans = [-9999]

    height(root, ans)

    return ans[0]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameter(root))
