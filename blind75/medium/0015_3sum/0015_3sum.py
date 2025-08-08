# LeetCode 15. 3Sum
# Difficulty: Medium
# Runtime: 551ms, Beats 93.35%/ Memory: 18.48MB, Beats 39.65%

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # If current number is greater than 0, no need to continue (sum can't be zero)
            if nums[i] > 0:
                break
            # Skip duplicate starting elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates on the left side
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates on the right side
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res

        