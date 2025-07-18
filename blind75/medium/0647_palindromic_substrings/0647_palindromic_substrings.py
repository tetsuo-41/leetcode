# LeetCode 5. Longest Palindromic Substring
# Difficulty: Medium
# Runtime: 163ms, Beats 66.58%/ Memory: 12.37MB, Beats 90.35%

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def expandAroundCenter(left, right):
            count = 0
            # Expand window outward as long as left=right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        res = 0
        for i in range(len(s)):
            # Count for odd and even palindrome
            res += expandAroundCenter(i, i)
            res += expandAroundCenter(i, i+1)
        return res

        