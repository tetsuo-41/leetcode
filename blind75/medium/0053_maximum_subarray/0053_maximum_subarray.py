# LeetCode 53. Maximum Subarray
# Difficulty: Medium
# Runtime: 90ms, Beats 42.72%/ Memory: 21.11MB, Beats 79.25%

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
