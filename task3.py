class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:
    def __init__(self):
        self.root = None

    def sum_values(self, node):
        if node is None:
            return 0
        return node.value + self.sum_values(node.left) + self.sum_values(node.right)


bst = BST()
bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.left.left = Node(2)
bst.root.left.right = Node(7)
bst.root.right.right = Node(20)

print("Сума всіх значень в дереві:", bst.sum_values(bst.root))
