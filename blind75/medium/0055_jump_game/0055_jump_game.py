# LeetCode 55. Jump Game
# Difficulty: Medium
# Runtime: 29ms, Beats 60.88%/ Memory: 13.09MB, Beats 98.96%

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest = 0
        for i, num in enumerate(nums):
            if i > furthest:
                return False
            else:
                furthest = max(furthest, i + num)
        return True