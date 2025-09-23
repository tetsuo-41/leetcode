# LeetCode 62. Unique Paths
# Difficulty: Medium
# Runtime: 0ms, Beats 100.00%/ Memory: 12.37MB, Beats 85.36%

import math

class Solution(object):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    def uniquePaths(self, m, n):
        return math.factorial(m+n-2) // (math.factorial(m-1) * math.factorial(n-1))
