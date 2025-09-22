# LeetCode 56. Merge Intervals
# Difficulty: Medium
# Runtime: 7ms, Beats 96.13%/ Memory: 16.04MB, Beats 67.31%

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 開始時間でソート
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # マージ結果が空 or 重ならない場合
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 重なる場合 → 結合（end の最大値を更新）
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
