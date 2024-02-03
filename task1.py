class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.value


class BST:
    def __init__(self):
        self.root = None


bst = BST()
bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.right.right = Node(20)

print("Найбільше значення в дереві:", find_max(bst.root))
