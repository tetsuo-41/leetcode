# LeetCode 141. Linked List Cycle
# Difficulty: Easy
# Runtime: 37ms, Beats 57.74%/ Memory: 19.46MB, Beats 85.30%


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True # Cycle detected

        return False # reached end, no cycle