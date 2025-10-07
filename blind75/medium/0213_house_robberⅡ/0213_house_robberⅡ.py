# LeetCode 213. House Robber II
# Difficulty: Medium
# Runtime: 0ms, Beats 100.00%/ Memory: 12.50MB, Beats 16.01%

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 要素が1つだけならそれを返す
        if len(nums) == 1:
            return nums[0]

        # 通常のHouse Robber（線形）を解く関数
        def rob_line(houses):
            prev1, prev2 = 0, 0
            for num in houses:
                prev1, prev2 = max(prev1, prev2 + num), prev1
            return prev1

        # ① 最初の家を含む場合（最後を除く）
        case1 = rob_line(nums[:-1])
        # ② 最後の家を含む場合（最初を除く）
        case2 = rob_line(nums[1:])

        return max(case1, case2)
