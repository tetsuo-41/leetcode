# LeetCode 207. Course Schedule
# Difficulty: Medium
# Runtime: 11ms, Beats 45.88%/ Memory: 16.02MB, Beats 33.78%

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict

        # グラフ構築
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        # 0 = 未訪問, 1 = 探索中, 2 = 完了
        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 1:  # 探索中に再訪問 → サイクル
                return False
            if visited[node] == 2:  # すでに完了済み → 問題なし
                return True

            visited[node] = 1  # 探索中にマーク
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 2  # 探索完了
            return True

        # すべてのノードを確認（非連結グラフ対応）
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
