# 🧩 問題名: [1. Two Sum](https://leetcode.com/problems/two-sum/)

## 📝 問題概要

整数の配列 `nums` と整数 `target` が与えられる。  
配列の中から**合計が target になる 2 つの要素**を探し、そのインデックスを返す問題。

- 答えは必ず1つ存在する。
- 同じ要素を2回使うことはできない。
- インデックスの順番は任意。

### 🔍 例
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
Explanation: nums[0] + nums[1] == 9

## ✅ 解法方針（Approach）

### 💡 コアアイデア
- target - num で「あと何が必要か？」（complement）を求める。
- 各数字を見たときに complement が辞書（num_dict）にすでにあれば、それが答え。
- 辞書には「数値 → インデックス」を記録し、探索を O(1) にする。

### 🧠 なぜ辞書を使う？
→ complement を探すとき、リストをループして探すと O(n) かかり、最初の数字から最後まで繰り返すと、O(n^2) になるが、辞書なら一瞬（O(1)）。  
その結果、全体の計算量が O(n) になる。なぜなら辞書はキーをハッシュ関数で数値（一次元座標のように）に変換し、直接その位置を探しに行く仕組みだから。

## ⏱️ 時間計算量
 • 時間計算量: O(n)  
 • 空間計算量: O(n)（補数を記録する辞書を使うため）

## 🧠 ポイントと学び
 • 何をすぐ探したいか？を意識すると dict / set が使える場面が見えてくる。  
 • リストを2重ループで探すより、「補数を先に記録しておく」発想が大事。  
 • 「あと何が必要か？」を考える癖はアルゴリズム設計で超重要。

## 📈 提出結果
 • Runtime: 0ms (Beats 100.00%)
 • Memory: 13.15MB (Beats 61.10%)

---

