# 🧩 問題名: [55. Jump Game](https://leetcode.com/problems/jump-game/)

## 📝 問題概要

整数配列 `nums` が与えられる。  
各要素 `nums[i]` は、その位置から最大で何マス先にジャンプできるかを表す。  
最初は `index = 0` に位置しており、**最後のインデックスに到達できるかどうか**を判定せよ。

### 🔍 例
Input: nums = [2,3,1,1,4]  
Output: true  
Explanation: index0 → 1（ジャンプ1）→ 4（ジャンプ3）

Input: nums = [3,2,1,0,4]  
Output: false  
Explanation: index0 → 3 に到達するが、その値が 0 なので前に進めない。

---

## ✅ 解法方針（Approach）

### 💡 コアアイデア
- **貪欲法 (Greedy)** を使う。
- `furthest` = 現時点で到達可能な最も遠い位置を管理。
- 各インデックス `i` を走査し、もし `i` が `furthest` を超えていたら到達不可能 → False。
- そうでなければ `furthest = max(furthest, i + nums[i])` を更新していく。
- 最終的に `furthest >= 最後のindex` なら True。

### 🧠 ポイント
- 「最短経路」ではなく「到達可能性」が問われているため、  
  **可能な範囲を1本の線として更新していく**のが最適解。
- DPでも解けるが、Greedyにすれば O(n) にできる。

---

## ⏱️ 計算量
- 時間計算量: O(n)（1度の走査）
- 空間計算量: O(1)（定数領域）

---

## 🧠 ポイントと学び
- **到達可能性系の問題は Greedy で「最も遠く」を追跡するのが定石**。
- 「その場で詰むかどうか」を見抜くことで効率的に判定できる。

---

## 📈 提出結果
- Runtime: 29ms (Beats 60.88%)  
- Memory: 13.09MB (Beats 98.96%)

---

