# LeetCode 217. Contains Duplicate
# Difficulty: Easy
# Runtime: 23ms, Beats 32.21%/ Memory: 25.80MB, Beats 69.76%

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # setに変換して要素数を比較
        return len(nums) != len(set(nums))