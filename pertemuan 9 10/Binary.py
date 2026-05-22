# Identitas
print("Nama : Syahirah Yusriyah Putri")
print("NIM  : J0403251003")
print("=" * 40)



class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Fungsi insert
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    # Inorder: Left - Root - Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # Preorder: Root - Left - Right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    # Postorder: Left - Right - Root
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(3)
data = [33, 23, 23, 43, 13, 33, 38]

for d in data:
    root.insert(d)

# Output traversal
print("\nInorder  :", root.inorderTraversal(root))
print("Preorder :", root.preorderTraversal(root))
print("Postorder:", root.postorderTraversal(root))