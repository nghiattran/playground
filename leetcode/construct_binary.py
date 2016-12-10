class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

count = 0

def buildTree(preorder, inorder, start = 0, end = None, count = 0):
    if end is None:
        end = len(inorder) - 1
    if start > end:
        return  None
    print(preorder[start], start, end)
    root = TreeNode(preorder[start])
    if start == end or count == 3:
        return root

    left_num = inorder.index(preorder[start]) + 1 - start
    # print(inorder.index(preorder[start]))

    print(preorder[start], start + left_num, end, start + 1, start + left_num - 1)
    root.left = buildTree(preorder, inorder, start + 1, start + left_num - 1, count + 1)
    root.right = buildTree(preorder, inorder, start + left_num, end, count + 1)

    return root

preorder = [ 'F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
inorder = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
root = buildTree(preorder, inorder)

print(root.val)
print(root.right.right.val)
print(root.left.right.val)