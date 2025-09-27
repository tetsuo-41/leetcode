# LeetCode 322. Coin Change
# Difficulty: Medium
# Runtime: 854ms, Beats 53.54%/ Memory: 13.10MB, Beats 34.33%

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 初期化: amount+1を「作れない値」の代わりに置く
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0  # 金額0はコイン0枚で作れる

        # DPループ
        for x in range(1, amount + 1):
            for c in coins:
                if x - c >= 0:
                    dp[x] = min(dp[x], dp[x - c] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1
