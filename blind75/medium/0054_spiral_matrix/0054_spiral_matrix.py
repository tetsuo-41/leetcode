# LeetCode 54. Spiral Matrix
# Difficulty: Medium
# Runtime: 0ms, Beats 100.00%/ Memory: 12.35MB, Beats 84.20%

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 上の行
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # 右の列
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 下の行
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # 左の列
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
