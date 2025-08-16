# LeetCode 19. Remove Nth Node From End of List
# Difficulty: Medium
# Runtime: 0ms, Beats 100.00%/ Memory: 19.51MB, Beats 19.87%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = slow = dummy

        # fastをn+1ステップ進める（削除対象の1つ前にslowが来るようにする）
        for _ in range(n + 1):
            fast = fast.next

        # fastが末尾に到達するまで進める
        while fast:
            fast = fast.next
            slow = slow.next

        # slow.next を削除
        slow.next = slow.next.next

        return dummy.next
