# LeetCode 133. Graph clone
# Difficulty: Medium
# Runtime: 39ms, Beats 28.72%/ Memory: 12.83MB, Beats 24.62%

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        visited = {}

        def dfs(current):
            # If the node was already cloned, return the clone
            if current in visited:
                return visited[current]
            # Clone the current node
            copy = Node(current.val)
            visited[current] = copy
            # Recursively clone all the neighbors
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)

        