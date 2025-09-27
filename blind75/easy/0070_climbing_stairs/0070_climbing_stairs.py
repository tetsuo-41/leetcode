# LeetCode 70. Climbing Stairs
# Difficulty: Easy
# Runtime: 0ms, Beats 100.00%/ Memory: 12.30MB, Beats 98.77%

class Solution(object):
      def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        # f(1) = 1, f(2) = 2
        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second
        return second

#↓↓↓数式解法：Binetの公式（O(1)）
import math

class Solution(object):
    def climbStairs(self, n):
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return int(round((phi**(n+1) - psi**(n+1)) / sqrt5))
