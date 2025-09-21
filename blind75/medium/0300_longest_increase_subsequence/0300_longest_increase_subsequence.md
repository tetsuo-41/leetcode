# 🧩 問題名: [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

## 📝 問題概要

整数配列 `nums` が与えられる。  
その中から取り出せる **最長の厳密に増加する部分列（subsequence）** の長さを求めよ。  

※ subsequence とは、要素を削除しても良いが順番は変えられない部分列のこと。

### 🔍 例
Input: nums = [10,9,2,5,3,7,101,18]  
Output: 4  
Explanation: 最長増加部分列は [2,3,7,101] → 長さ 4  

Input: nums = [0,1,0,3,2,3]  
Output: 4  

Input: nums = [7,7,7,7,7,7,7]  
Output: 1  

---

## ✅ 解法方針（Approach）

### 💡 コアアイデア
この問題の解法は大きく2つに分けられる：

1. **DP（O(n²) 解法）**  
   - `dp[i]` を「`nums[i]` を末尾とする最長増加部分列の長さ」と定義する。  
   - 各 `i` について、`j < i` かつ `nums[j] < nums[i]` であれば `dp[i] = max(dp[i], dp[j] + 1)` と更新する。  
   - 配列全体で最大値を取れば答え。  

2. **バイナリサーチを用いた O(n log n) 解法**  
   - 1つの配列 `sub` を用意し、「これまで見つけた増加部分列の最小末尾」を管理する。  
   - 各 `num` に対して：
     - `sub` の末尾より大きければ追加する。
     - そうでなければ `bisect_left` で置き換える位置を二分探索して更新する。  
   - `sub` の長さがそのまま答えになる。  
   - 問題は「strictly increasing（厳密に増加）」なので`bisect_left`だが「non-decreasing（非減少）」の場合は`bisect_right`を使う。

### 🧠 DP と O(n log n) の違い
- DPは分かりやすいが O(n²) かかるので、入力が大きいとTLEになる可能性がある。  
- 二分探索を使うと O(n log n) に改善でき、実用的。  

---

## ⏱️ 計算量
- DP 解法  
  • 時間計算量: O(n²)  
  • 空間計算量: O(n)  

- バイナリサーチ解法  
  • 時間計算量: O(n log n)  
  • 空間計算量: O(n)  

---

## 🧠 ポイントと学び
- subsequence の問題は「DP」か「二分探索テクニック」を使うことが多い。  
- 「最長増加部分列 (LIS)」は典型問題で、他のDP・グラフ問題の基礎にもなる。  
- 二分探索法は「末尾を最小化して管理」するのがコツ。  

---

## 📈 提出結果
（バイナリサーチ解法の場合）  
 • Runtime: 7ms (Beats 93.94%)  
 • Memory: 12.81MB (Beats 37.18%)  

---