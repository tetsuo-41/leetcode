# LeetCode 198. House Robber
# Difficulty: Medium
# Runtime: 0ms, Beats 100.00%/ Memory: 12.51MB, Beats 14.97%

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, curr

        return prev1
