# LeetCode 424. Longest Repeating Character Replacement
# Difficulty: Medium
# Runtime: 116ms, Beats 84.55%/ Memory: 15.40MB, Beats 47.06%

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        left = 0
        max_count = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # 条件を満たさない場合は左を縮める
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res