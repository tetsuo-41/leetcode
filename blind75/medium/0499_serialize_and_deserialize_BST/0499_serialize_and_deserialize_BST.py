# LeetCode 449. Serialize and Deserialize BST
# Difficulty: Medium
# Runtime: 46ms, Beats 94.20%/ Memory: 20.32MB, Beats 62.32%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder(node):
            if not node:
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        preorder = list(map(int, data.split(',')))
        self.idx = 0

        def build(min_val, max_val):
            if self.idx >= len(preorder):
                return None
            val = preorder[self.idx]
            if val < min_val or val > max_val:
                return None
            self.idx += 1
            node = TreeNode(val)
            node.left = build(min_val, val)
            node.right = build(val, max_val)
            return node

        return build(float('-inf'), float('inf'))
