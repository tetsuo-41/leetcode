# LeetCode 213. House Robber II
# Difficulty: Medium
# Runtime: 4ms, Beats 27.67%/ Memory: 12.52MB, Beats 28.38%

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not s or s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # 空文字の初期化
        dp[1] = 1  # 最初の文字が '0' でないことは確認済み

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])       # 1桁
            two_digits = int(s[i - 2:i])    # 2桁

            # 1桁が有効（'1'〜'9'）
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]

            # 2桁が有効（'10'〜'26'）
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

#↓↓↓O(1)最適化版
class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        
        prev2, prev1 = 1, 1  # dp[i-2], dp[i-1]
        for i in range(1, len(s)):
            curr = 0
            one_digit = int(s[i])
            two_digits = int(s[i-1:i+1])

            if 1 <= one_digit <= 9:
                curr += prev1
            if 10 <= two_digits <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1
