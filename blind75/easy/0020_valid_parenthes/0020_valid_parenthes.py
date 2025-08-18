# LeetCode 20. Valid Parentheses
# Difficulty: Easy
# Runtime: 3ms, Beats 52.75%/ Memory: 12.56MB, Beats 56.88%

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # 閉じ括弧 -> 開き括弧 の対応
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():
                # 開き括弧ならスタックに積む
                stack.append(char)
            else:
                # 閉じ括弧の場合
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        # 最後にスタックが空なら全て対応している
        return not stack