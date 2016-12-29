import math

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        slow = fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        if fast is not None:
            slow = slow.next

        if slow is None:
            return True

        slow = self.reverse(slow)

        while slow is not None:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverse(self, head):
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(2)
node5 = ListNode(1)
node6 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(Solution().isPalindrome(node1))