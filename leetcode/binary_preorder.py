class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def preorderTraversal(self, root, res=[]):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
      return []

    res.append(root.val)
    self.preorderTraversal(root.left, res)
    self.preorderTraversal(root.right, res)
    return res

nodes = []
for i in range(9):
  nodes.append(TreeNode(i + 1))

nodes[0].left = nodes[1]
# nodes[0].right = nodes[5]
# nodes[1].left = nodes[2]
# nodes[1].right = nodes[3]
# nodes[3].right = nodes[4]
# nodes[4].left = nodes[7]
# nodes[4].right = nodes[8]

print(Solution().preorderTraversal(nodes[0]))