# LeetCode 3. Longest Substring Without Repeating Character
# Difficulty: Medium
# Runtime: 16ms, Beats 85.71%/ Memory: 12.61MB, Beats 73.13%

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last index of each character
        char_index_map = {}
        max_length = 0
        start = 0 #Left boundary of current window

        # Iterate over the string
        for i, char in enumerate(s):
            # If the character is already seen and its index is on or after the start, move the start to the next position of the last occurrence
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            # Update the last index of the character
            char_index_map[char] = i
            # Update the max length if needed
            max_length = max(max_length, i - start + 1)
        return max_length