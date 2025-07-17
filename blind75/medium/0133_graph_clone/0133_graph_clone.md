# 🧩 問題名: [133. Clone Graph](https://leetcode.com/problems/clone-graph/)

## 📝 問題概要

接続した無向のグラフが一つ上に与えられる。
そのグラフを**深いコピー (deep copy)** した結果を返せ。

グラフの各ノードは値 `val` と隣接ノードのリスト `neighbors` を持つ:

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

### 🔍 例
#### Example 1:
Input: `adjList = [[2,4],[1,3],[2,4],[1,3]]`
Output: `[[2,4],[1,3],[2,4],[1,3]]`

#### Example 2:
Input: `adjList = [[]]`
Output: `[[]]`

#### Example 3:
Input: `adjList = []`
Output: `[]`

## ✅ 解法方針 (Approach)

### 💡 コアアイデア
DFS (Depth-First Search)で、同じノードを二度複製しないように、既にクローンしたノードを `visited` に保存しながら深層変換する。
ノードを複製するたびに、隣接ノードもループ内で複製して接続を再現する。

### 🧠 なぜ DFS？
全ノードを1回ずつたどってコピーしたいので、DFS（深さ優先探索）または BFS（幅優先探索）で実装されるのが一般的。
再帰ベースなので DFS の方が実装が簡単。

## ⏱️ 計算量
時間計算量: O(N)
N: ノード数
空間計算量: O(N)
複製用の visited ディクショナリの分

## 🧠 ポイントと学び
**同じノードの二重複製を避けるために visited を使う**のが必要
**DFS / BFS** の再度的スキャンでは、グラフの複製などで実際によく使うテクニック

## 📈 提出結果
Runtime: 39ms (Beats 28.72%)
Memory: 12.83MB (Beats 24.62%)
