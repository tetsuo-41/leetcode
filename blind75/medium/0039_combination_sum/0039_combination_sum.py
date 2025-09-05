# LeetCode 39. Combination Sum
# Difficulty: Medium
# Runtime: 7ms, Beats 95.58%/ Memory: 12.50MB, Beats 52.31%

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()  # ソートしておくと、後で num > remain のとき break できる

        def dfs(start, path, remain):
            if remain == 0:
                res.append(list(path))
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remain:
                    break  # これ以降はすべて大きすぎるので枝を切る
                
                path.append(num)                   # ① 選ぶ
                dfs(i, path, remain - num)         # ② 探索（i渡し＝同じ要素の再利用OK）
                path.pop()                         # ③ 戻す

        dfs(0, [], target)
        return res
