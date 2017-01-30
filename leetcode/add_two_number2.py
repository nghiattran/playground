class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def connect(self, node):
      self.next = node
      return node

    def printList(self):
      cur = self
      while cur:
        print(cur.val, ' ', end="")
        cur = cur.next
      print()


class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    pointer = l1
    x1 = 0
    while pointer:
      x1 = x1 * 10 + pointer.val
      pointer = pointer.next

    pointer = l2
    x2 = 0
    while pointer:
      x2 = x2 * 10 + pointer.val
      pointer = pointer.next

    sum = x1 + x2

    head = ListNode(0)
    if sum == 0: return ListNode(0)
    while sum > 0:
      val, sum = sum % 10, int(sum / 10)
      node = ListNode(val)
      node.next = head
      head = node

    return head

l1 = ListNode(5)
l1.connect(ListNode(2)).connect(ListNode(4)).connect(ListNode(3))

l2 = ListNode(5)
l2.connect(ListNode(6)).connect(ListNode(4))

l3 = Solution().addTwoNumbers(l1, l2)
print(l3.printList())