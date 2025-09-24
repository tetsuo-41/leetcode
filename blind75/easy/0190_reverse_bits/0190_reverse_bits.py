# LeetCode 190. Reverse Bits
# Difficulty: Easy
# Runtime: 14ms, Beats 79.85%/ Memory: 12.55MB, Beats 7.52%

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for _ in range(32):
            # res を左に1ビットシフトし、n の最下位ビットを追加
            res = (res << 1) | (n & 1)
            # n を右に1ビットシフトして次へ
            n >>= 1
        return res
