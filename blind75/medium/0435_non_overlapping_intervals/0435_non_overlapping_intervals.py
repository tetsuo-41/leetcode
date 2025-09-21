# LeetCode 435. Non-overlapping Intervals
# Difficulty: Medium
# Runtime: 179ms, Beats 37.69%/ Memory: 45.22MB, Beats 53.96%

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # 終了時間でソート
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            # 重なりあり
            if intervals[i][0] < prev_end:
                count += 1
            else:
                prev_end = intervals[i][1]

        return count
