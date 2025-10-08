# LeetCode 226. Invert Binary Tree
# Difficulty: Easy
# Runtime: 0ms, Beats 100.00%/ Memory: 12.59MB, Beats 30.85%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        # 左右の子ノードをスワップ
        root.left, root.right = root.right, root.left

        # 再帰的に子ノードを反転
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
