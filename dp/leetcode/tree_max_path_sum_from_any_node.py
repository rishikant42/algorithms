class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def solve(root, ans):
    if root == None:
        return 0

    left = solve(root.left, ans)
    right = solve(root.right, ans)

    temp = max(
        max(left, right)+root.data,
        root.data
    )

    ans[0] = max(
        temp, left+right+root.data)

    return temp


def max_path(root):
    ans = [-999999]

    solve(root, ans)

    return ans[0]


root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);

print(max_path(root))
