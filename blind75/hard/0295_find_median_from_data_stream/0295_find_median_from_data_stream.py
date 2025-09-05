# LeetCode 295. Find Median from Data Stream
# Difficulty: Hard
# Runtime: 762ms, Beats 51.25%/ Memory: 35.44MB, Beats 76.32%

import heapq

class MedianFinder(object):

    def __init__(self):
        self.left = []  # max-heap (store as negative values)
        self.right = [] # min-heap

    def addNum(self, num):
        # まず最大ヒープ(left)に追加
        heapq.heappush(self.left, -num)

        # leftの最大値 <= rightの最小値 という関係を保つ
        if self.left and self.right and (-self.left[0]) > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        # サイズ差が1を超えないように調整
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0
