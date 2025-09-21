# LeetCode 48. Rotate Image
# Difficulty: Medium
# Runtime: 0ms, Beats 100.00%/ Memory: 12.44MB, Beats 53.87%

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Step 1: 転置 (i < j のときだけ swap)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: 各行を反転
        for row in matrix:
            row.reverse()
