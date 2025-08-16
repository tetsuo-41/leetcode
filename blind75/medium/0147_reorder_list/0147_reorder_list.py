# LeetCode 133. Graph clone
# Difficulty: Medium
# Runtime: 5ms, Beats 80.92%/ Memory: 30.07MB, Beats 87.54%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    """
    :type head: Optional[ListNode]
    :rtype: None Do not return anything, modify head in-place instead.
    """
    def reorderList(self, head):
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for v in arr[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def to_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

if __name__ == "__main__":
    s = Solution()
    for arr in ([1,2,3,4], [1,2,3,4,5], [1], [1,2]):
        h = build_list(arr)
        s.reorderList(h)
        print(arr, "->", to_list(h))