# LeetCode 49. Group Anagrams
# Difficulty: Medium
# Runtime: 13ms, Beats 97.87%/ Memory: 16.09MB, Beats 80.68%

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))  # ソートした文字列をキーにする
            groups[key].append(word)
        return list(groups.values())
