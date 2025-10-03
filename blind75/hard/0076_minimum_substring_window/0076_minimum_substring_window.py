# LeetCode 76. Minimum Window Substring
# Difficulty: Hard
# Runtime: 123ms, Beats 46.67%/ Memory: 12.64MB, Beats 75.58%

from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        need = Counter(t)  # tの必要文字カウント
        have = {}
        required = len(need)
        formed = 0  # 条件を満たした種類数

        l, r = 0, 0
        ans = float("inf"), None, None  # (長さ, 左, 右)

        while r < len(s):
            c = s[r]
            have[c] = have.get(c, 0) + 1

            if c in need and have[c] == need[c]:
                formed += 1

            # すべての文字を含むウィンドウなら縮めてみる
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # 左ポインタを動かして縮める
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
