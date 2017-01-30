class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack = []
    current = root
    res = []
    while current is not None:
      if current.left is not None:
        stack.append(current)
        tmp = current
        current = current.left
        tmp.left = None
      else:
        res.append(current.val)
        if current.right is None:
          if len(stack) == 0:
            return res
          current = stack.pop()
        else:
          current = current.right
    return res

nodes = []
for i in range(9):
  nodes.append(TreeNode(i + 1))

nodes[0].left = nodes[1]
nodes[0].right = nodes[5]
nodes[1].left = nodes[2]
nodes[1].right = nodes[3]
nodes[3].right = nodes[4]
nodes[4].left = nodes[7]
nodes[4].right = nodes[8]

print(Solution().inorderTraversal(nodes[0]))