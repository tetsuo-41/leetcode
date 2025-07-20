# LeetCode 268. Missing Number
# Difficulty: Medium
# Runtime: 0ms, Beats 100.00%/ Memory: 13.42MB, Beats 29.99%

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum