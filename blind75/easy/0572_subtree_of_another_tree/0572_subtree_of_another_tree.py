# LeetCode 56. Merge Intervals
# Difficulty: Easy
# Runtime: 75ms, Beats 77.89%/ Memory: 13.89MB, Beats 19.39%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    """
    :type root: Optional[TreeNode]
    :type subRoot: Optional[TreeNode]
    :rtype: bool
    """
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return (self.isSameTree(s.left, t.left) and 
                self.isSameTree(s.right, t.right))
