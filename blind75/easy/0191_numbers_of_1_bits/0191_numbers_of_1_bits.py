# LeetCode 191. Number of 1 Bits
# Difficulty: Easy
# Runtime: 0ms, Beats 100.00%/ Memory: 12.52MB, Beats 9.27%

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 方法1: 組み込み関数利用
        return bin(n).count('1')

        # 方法2: ビット演算
        # count = 0
        # while n:
        #     n &= n - 1
        #     count += 1
        # return count