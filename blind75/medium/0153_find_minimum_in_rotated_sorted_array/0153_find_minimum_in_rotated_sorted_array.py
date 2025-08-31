# LeetCode 153. Find Minimum in Rotated Sorted Array
# Difficulty: Hard
# Runtime: 1ms, Beats 9.25%/ Memory: 12.42MB, Beats 92.00%

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # 最小値は右側にある
                left = mid + 1
            else:
                # 最小値は左側を含む
                right = mid

        return nums[left]
