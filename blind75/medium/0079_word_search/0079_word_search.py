# LeetCode 73. Set Matrix Zeroes
# Difficulty: Medium
# Runtime: 5426ms, Beats 86.69%/ Memory: 12.49MB, Beats 52.47%

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        
        def dfs(i, j, k):
            if not (0 <= i < m and 0 <= j < n):  # 範囲外チェック
                return False
            if board[i][j] != word[k]:  # 文字が一致しない場合
                return False
            if k == len(word) - 1:  # 最後の文字まで一致したら True
                return True
            
            tmp, board[i][j] = board[i][j], "#"  # 一時マーク（訪問済み）
            res = (dfs(i+1, j, k+1) or
                   dfs(i-1, j, k+1) or
                   dfs(i, j+1, k+1) or
                   dfs(i, j-1, k+1))
            board[i][j] = tmp  # バックトラック
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
