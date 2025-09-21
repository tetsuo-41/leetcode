# LeetCode 300. Longest Increasing Subsequence
# Difficulty: Medium
# Runtime: 7ms, Beats 93.94%/ Memory: 12.81MB, Beats 37.18%

import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub = []
        for num in nums:
            # 挿入位置を二分探索で取得
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)  # 末尾に追加
            else:
                sub[i] = num  # 置き換えで末尾を小さく維持
        return len(sub)

#↓↓↓ O(n²) DP 解法
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n  # 各位置を末尾とする LIS の長さを格納

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)