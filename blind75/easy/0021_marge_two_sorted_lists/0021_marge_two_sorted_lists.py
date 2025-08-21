# LeetCode 21. Merge Two Sorted Lists
# Difficulty: Easy
# Runtime: 0ms, Beats 100.00%/ Memory: 12.42MB, Beats 75.53%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()   # ダミーノード
        tail = dummy         # 結果リストの末尾を指すポインタ

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # tailを更新

        # どちらかが残っていれば繋げる
        tail.next = list1 if list1 else list2

        return dummy.next  # 先頭ノードを返す
