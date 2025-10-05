# LeetCode 338. Counting Bits
# Difficulty: Easy
# Runtime: 3ms, Beats 99.39%/ Memory: 17.83MB, Beats 48.54%

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans