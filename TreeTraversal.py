class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def TraverseToList(node):
    if node == None : return []
    return TraverseToList(node.left) + [node.value] + TraverseToList(node.right)

def HeightOfTree(node):
    if node == None : return 0
    return 1 + max(HeightOfTree(node.right), HeightOfTree(node.left))


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

print(TraverseToList(root))
print(HeightOfTree(root))