# LeetCode 1. Two Sum
# Difficulty: Easy
# Runtime: 0ms, Beats 100.00%/ Memory: 13.15MB, Beats 61.10%

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create a dictionary to store numbers we've seen and their indices
        num_dict = {}

        # Iterate over the list once
        for i, num in enumerate(nums):
            # Calculate the complement that would sum up to the target
            complement = target - num

            # If the complement is already in the dictionary, return the pair of indices
            if complement in num_dict:
                return [num_dict[complement], i]

            # Otherwise, store the current number and its index in the dictionary
            num_dict[num] = i

        # According to the problem statement, exactly one solution always exists
