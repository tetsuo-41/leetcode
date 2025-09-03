# LeetCode 417. Pacific Atlantic Water Flow
# Difficulty: Medium
# Runtime: 35ms, Beats 90.19%/ Memory: 13.94MB, Beats 46.45%

#↓BFS版
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        from collections import deque

        # BFS 用の関数
        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):  # 逆流条件
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        # 太平洋に接するセル
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        # 大西洋に接するセル
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]

        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)

        # 両方に到達できるセルの交差を返す
        result = list(map(list, pacific_reachable & atlantic_reachable))
        return result


#↓DFS版
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def dfs(r, c, visited, prev_height):
            # 範囲外 or すでに訪問済み or 逆流できない → ストップ
            if (r < 0 or r >= m or c < 0 or c >= n or
                (r, c) in visited or heights[r][c] < prev_height):
                return
            visited.add((r, c))
            # 4方向に進む
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        pacific_reachable, atlantic_reachable = set(), set()

        # 太平洋に接するセルから DFS
        for c in range(n):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(m - 1, c, atlantic_reachable, heights[m - 1][c])
        for r in range(m):
            dfs(r, 0, pacific_reachable, heights[r][0])
            dfs(r, n - 1, atlantic_reachable, heights[r][n - 1])

        result = list(map(list, pacific_reachable & atlantic_reachable))
        return result
