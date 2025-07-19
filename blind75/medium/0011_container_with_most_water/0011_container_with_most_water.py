# LeetCode 11. Container With Most Water
# Difficulty: Medium
# Runtime: 123ms, Beats 17.65%/ Memory: 20.83MB, Beats 14.09%

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current height and width
            h = min(height[left], height[right])
            w = right - left
            # Update the maximum area found so far
            max_area = max(max_area, h*w)
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area