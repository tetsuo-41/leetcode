# LeetCode 213. House Robber II
# Difficulty: Medium
# Runtime: 19ms, Beats 20.33%/ Memory: 20.00MB, Beats 5.96%

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 出現回数をカウント
        count = Counter(nums)
        
        # 出現回数をインデックスに持つバケットを作成
        freq = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)
        
        # 出現回数の多い順に結果を追加
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
