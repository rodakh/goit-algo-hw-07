class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value


class BST:
    def __init__(self):
        self.root = None


bst = BST()
bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.left.left = Node(2)

print("Найменше значення в дереві:", find_min(bst.root))
