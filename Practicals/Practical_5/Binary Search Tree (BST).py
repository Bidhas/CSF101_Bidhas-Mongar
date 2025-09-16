class node:
    def init (self,value):
        self.value = value 
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert (self, value):
        if not self.root:
            self.root
            self.root = node(value)
        else:
            self._insert_recursive(self.root, value)

def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = node(value)
            else:
                self._insert_recursive(node.right, value)
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst. insert(value)
