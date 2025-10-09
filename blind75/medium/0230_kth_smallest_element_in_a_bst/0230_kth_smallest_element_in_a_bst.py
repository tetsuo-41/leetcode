# LeetCode 230. Kth Smallest Element in a BST
# Difficulty: Medium
# Runtime: 0ms, Beats 100.00%/ Memory: 20.32MB, Beats 24.81%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = []
        while True:
            # 左端まで辿る
            while root:
                stack.append(root)
                root = root.left
            # 左端に到達したら pop
            root = stack.pop()
            k -= 1
            # k 回目の pop なら答え
            if k == 0:
                return root.val
            # 右部分木へ移動
            root = root.right
