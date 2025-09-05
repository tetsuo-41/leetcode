# 🧩 問題名: [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

## 📝 問題概要

データストリーム（順に与えられる整数列）が与えられる。  
途中の状態で**中央値（median）**を効率的に求めるクラス `MedianFinder` を実装せよ。  

- 中央値とは：
  - 配列サイズが奇数 → ソート後の中央の値  
  - 配列サイズが偶数 → ソート後の中央2つの平均値  

### 実装仕様
- `MedianFinder()` → オブジェクトを初期化  
- `addNum(num: int)` → 新しい整数を追加  
- `findMedian()` → これまでの数列の中央値を返す  

### 🔍 例
Input:
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]

Output:
[null,null,null,1.5,null,2.0]

Explanation:
- addNum(1) → [1]  
- addNum(2) → [1,2]  
- findMedian() → (1+2)/2 = 1.5  
- addNum(3) → [1,2,3]  
- findMedian() → 2  

---

## ✅ 解法方針（Approach）

### 💡 コアアイデア
中央値を効率的に求めるには、単純にソートすると O(n log n) かかってしまう。  
ここでは **2つのヒープ（最大ヒープ + 最小ヒープ）** を用いて O(log n) で処理する。

1. **最大ヒープ (left)**  
   - 中央値より小さい値を保持  
   - Python では `heapq` が最小ヒープしかないため、負の値を入れて最大ヒープを実現  

2. **最小ヒープ (right)**  
   - 中央値より大きい値を保持  

3. バランス調整  
   - 2つのヒープのサイズ差が 1 以上にならないように調整する  

4. 中央値取得  
   - 要素数が奇数 → 要素数が多いヒープの先頭  
   - 要素数が偶数 → 両ヒープの先頭の平均値  

---

## ⏱️ 計算量
- **addNum**: O(log n)（ヒープ操作）
- **findMedian**: O(1)（ヒープ先頭を参照）
- 空間計算量: O(n)

---

## 🧠 ポイントと学び
- 中央値を動的に管理する典型問題。  
- ヒープを使うことで **逐次追加 + 中央値取得** を高速化できる。  
- Python の `heapq` は最小ヒープのみ → 最大ヒープは負値を使うテクニックが必須。  

---

## 📈 提出結果
- Runtime: 762ms (Beats 51.25%)  
- Memory: 35.44MB (Beats 76.32%)  
