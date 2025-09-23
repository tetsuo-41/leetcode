# 🧩 問題名: [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

## 📝 問題概要

2つの二分木 `root` と `subRoot` が与えられる。  
`subRoot` が `root` の部分木として存在する場合に `true` を返し、そうでなければ `false` を返せ。  

部分木とは、あるノードを根として、そのノードのすべての子孫を含む木のことを指す。  
なお、木そのものも自分自身の部分木とみなす。  

### 🔍 例
**例1**  
Input: root = [3,4,5,1,2], subRoot = [4,1,2]  
Output: true  

**例2**  
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]  
Output: false  

## ✅ 解法方針（Approach）

### 💡 コアアイデア
- `subRoot` が `root` の部分木であるためには、`root` 内のあるノードを根とする木が `subRoot` と**完全に一致**する必要がある。
- したがって次の2ステップで解ける：
  1. `root` のすべてのノードを走査して「ここを根とした部分木が `subRoot` と一致するか？」を調べる。
  2. 一致判定は「両方の木の構造と値が完全に同じか」を再帰で確認する。

### 🧠 判定の流れ
- もし `isSameTree(root, subRoot)` が真なら、その時点で `true` を返す。
- そうでなければ `root.left` と `root.right` に対して再帰的に探索を続ける。
- 全ての探索が終わっても一致が見つからなければ `false`。

### 🔑 ヘルパー関数
```python
def isSameTree(p, q):
    - 両方とも None → True
    - 片方だけ None → False
    - 値が異なる → False
    - それ以外 → 左右の子を再帰的に比較
```

## ⏱️ 計算量
- 時間計算量: O(m * n)
- n = root のノード数, m = subRoot のノード数
- 最悪の場合、root の全ノードに対して subRoot 全体を比較するため。

空間計算量: O(h) （h は再帰の深さ = 木の高さ）

## 🧠 ポイントと学び
- 部分木問題では「一致判定の再帰」と「全ノード探索」を組み合わせるのが定石。
- None チェックを丁寧に書くことでバグを防げる。
- DFS を基本として考えると整理しやすい。

---

## 📈 提出結果
- Runtime: 75ms (Beats 77.82%)  
- Memory: 13.89MB (Beats 19.39%)  

---
