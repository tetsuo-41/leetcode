# 🧩 問題名: [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## 📝 問題概要

整数の配列 `nums` が与えられる。  
連続する部分配列の中で、**合計が最大となる部分配列の和**を求めよ。

### 🔍 例
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]  
Output: 6  
Explanation: 最大部分配列は [4,-1,2,1] で、和は 6

Input: nums = [1]  
Output: 1  
Explanation: 配列が1要素の場合、その要素が最大部分配列

Input: nums = [5,4,-1,7,8]  
Output: 23  
Explanation: 最大部分配列は [5,4,-1,7,8] で、和は 23

## ✅ 解法方針（Approach）

### 💡 コアアイデア（Kadane’s Algorithm）
- 配列を左から順にスキャンし、現在の部分配列の和 `current_sum` を管理する。
- 新しい要素 `num` を見るたびに、  
  `current_sum = max(num, current_sum + num)`  
  と更新することで、**部分配列の開始点を動的に切り替え**られる。
- 同時に `max_sum` に `current_sum` を比較更新し、最大和を記録する。

### 🧠 Why max(num, current_sum + num) が重要？
→ 負の累積和が続く場合、新しい要素から部分配列を再スタートすることで、和を最大化できる。

---

## ⏱️ 計算量
- 時間計算量: O(n)
- 配列を1回走査するだけ
- 空間計算量: O(1)（変数2つのみ使用）

---

## 🧠 ポイントと学び
- 負の累積和が続く場合は部分配列をリセットする
- 1回の走査で最大部分配列を求める典型的手法：Kadane’s Algorithm
- DP的に「その時点での最適解」を保持する考え方が重要

---

## 📈 提出結果
- Runtime: 90ms (Beats 42.72%)  
- Memory: 21.11MB (Beats 79.25%)  

---