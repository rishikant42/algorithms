class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return -1
    return max(height(node.left), height(node.right)) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(12)
root.right.right = Node(13)

root.left.right.left = Node(6)
root.left.right.right = Node(7)

root.left.right.right.left = Node(8)
root.left.right.right.right = Node(9)

root.left.right.right.right.left = Node(10)
root.left.right.right.right.right = Node(11)

print(height(root))
