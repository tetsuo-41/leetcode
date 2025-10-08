# LeetCode 100. Same Tree
# Difficulty: Easy
# Runtime: 0ms, Beats 100.00%/ Memory: 12.50MB, Beats 86.29%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # どちらも存在しない場合 → 同じ木
        if not p and not q:
            return True
        
        # 一方のみ存在する or 値が異なる場合 → 違う木
        if not p or not q or p.val != q.val:
            return False
        
        # 左右の子ノードを再帰的に比較
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
