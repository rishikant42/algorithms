class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def solve(root, ans):
    if root == None:
        return 0

    left = solve(root.left, ans)
    right = solve(root.right, ans)

    temp = max(left, right)+root.data

    if root.left == None and root.right == None:
        temp = max(temp, root.data)

    ans[0] = max(
        temp, left+right+root.data)

    return temp


def max_path(root):
    ans = [-999999]

    solve(root, ans)

    return ans[0]


root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)
print(max_path(root))
