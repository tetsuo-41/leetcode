# 🧩 問題名: [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## 📝 問題概要

ソート済みの昇順配列が **1 回以上回転**（rotate）された配列 `nums` が与えられる。  
この配列から **最小の要素** を返せ。  

ただし、計算量は **O(log n)** でなければならない。

### 🔍 例
Input: nums = [3,4,5,1,2]  
Output: 1  
Explanation: 元の配列 [1,2,3,4,5] を3回回転したもの。

Input: nums = [4,5,6,7,0,1,2]  
Output: 0  
Explanation: 元の配列 [0,1,2,4,5,6,7] を4回回転したもの。

Input: nums = [11,13,15,17]  
Output: 11  
Explanation: 回転しても最小値は先頭のまま。

---

## ✅ 解法方針（Approach）

### 💡 コアアイデア
- 配列が部分的に「ソート済み区間」に分かれている点に注目。
- **二分探索**を利用して、最小値が含まれる区間を絞り込む。

### 🧩 アルゴリズム手順
1. `left = 0, right = len(nums) - 1` で初期化。
2. `mid = (left + right) // 2` を計算。
3. `nums[mid] > nums[right]` の場合  
   → 最小値は右側にあるので `left = mid + 1`。
4. それ以外の場合  
   → 最小値は左側にあるので `right = mid`。
5. `left == right` になったとき、その位置が最小値。

---

## ⏱️ 計算量
- 時間計算量: **O(log n)** （二分探索のため）
- 空間計算量: **O(1)**

---

## 🧠 ポイントと学び
- 「回転されたソート配列」は典型的な **二分探索応用問題**。
- `nums[mid] > nums[right]` の比較で、**どちら側に最小値があるか** を判定できるのが肝。
- 線形探索だと O(n) になるので、必ず二分探索で解く。

---
## 📈 提出結果

* Runtime: 1ms (Beats 9.25%)
* Memory: 12.42MB (Beats 92.00%)