# LeetCode 152. Maximum Product Subarray
# Difficulty: Medium
# Runtime: 10ms, Beats 61.45%/ Memory: 13.15MB, Beats 53.16%

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            # 負数のときに swap するのがポイント
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(num, num * max_prod)
            min_prod = min(num, num * min_prod)
            
            ans = max(ans, max_prod)
        
        return ans
