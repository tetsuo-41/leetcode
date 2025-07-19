# LeetCode 139. Word Break
# Difficulty: Medium
# Runtime: 0ms, Beats 100.00%/ Memory: 12.54MB, Beats 42.00%

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)  # Convert list to set for O(1) lookup
        n = len(s)
        max_len = max(map(len, wordDict)) if wordDict else 0  # Maximum length of words in the dictionary

        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always segmentable

        for i in range(1, n + 1):
            start = max(0, i - max_len)  # Limit the start index based on max word length
            for j in range(start, i):
                # Check if s[0:j] can be segmented and s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further if s[0:i] is segmentable

        return dp[n]  # Return whether the entire string can be segmented
