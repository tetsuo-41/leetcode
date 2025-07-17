# LeetCode 5. Longest Palindromic Substring
# Difficulty: Medium
# Runtime: 341ms, Beats 73.65%/ Memory: 12.44MB, Beats 79.43%

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            # Expand window outward as long as left=right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
            # Store the longest palindromic substring found so far
        longest = ""
        for i in range(len(s)):
        # Check for odd and even palindrome
            odd_palindrome = expandAroundCenter(i, i)
            even_palindrome = expandAroundCenter(i, i+1)

            current_longest = odd_palindrome if len(odd_palindrome) > len(even_palindrome) else even_palindrome
            # Update the longest palindrome if a longer one is found
            if len(current_longest) > len(longest):
                longest = current_longest
        return longest
        