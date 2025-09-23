# LeetCode 56. Merge Intervals
# Difficulty: Medium
# Runtime: 3ms, Beats 56.11%/ Memory: 14.29MB, Beats 48.57%

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        n = len(intervals)
        
        # newIntervalより前の区間を追加
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # 重なる区間をマージ(重なる区間が複数のときに対応するためwhile)
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        # 残りの区間を追加
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
