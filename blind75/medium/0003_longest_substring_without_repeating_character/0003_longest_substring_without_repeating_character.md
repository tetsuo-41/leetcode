# 🧩 問題名: [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 📝 問題概要

文字列 `s` が与えられる。  
その中から**重複しない文字からなる最長の部分文字列（substring）**の長さを求める問題。

- 部分文字列は連続している必要がある。
- subsequence（部分列）ではなく substring（部分文字列）である点に注意。

### 🔍 例
Input: s = "abcabcbb"  
Output: 3  
Explanation: "abc" が最長で長さ3

Input: s = "bbbbb"  
Output: 1  
Explanation: "b" が最長で長さ1

Input: s = "pwwkew"  
Output: 3  
Explanation: "wke" が最長で長さ3（"pwke" は部分列であって部分文字列ではない）


## ✅ 解法方針（Approach）

### 💡 コアアイデア
- **スライディングウィンドウ**を使って、重複のない部分文字列を動的に管理する。
- 文字の出現位置を辞書（`char_index_map`など）で記録。
- 同じ文字が現れたら「ウィンドウの左端」を更新し、その文字の次の位置から再開。


### 🧠 なぜスライディングウィンドウ？
→ 左右のポインタで「現在の部分文字列の範囲」を表し、重複が出たら左端を右にずらす。
これで全体を一度だけ見るだけで済み、**O(n)** で解ける。


## ⏱️ 計算量
 • 時間計算量: O(n)  
 • 空間計算量: O(min(n, m)) （mは文字の種類数。英字+記号など固定ならO(1)）


## 🧠 ポイントと学び
 • 部分文字列の問題は「開始位置と終了位置をどう動かすか」を考えると良い。  
 • 重複チェックをリストでやると遅いが、辞書（やset）でO(1)探索ができるので高速化できる。  
 • 部分文字列系は「スライディングウィンドウ＋ハッシュセット／辞書」が定石。


## 📈 提出結果
 • Runtime: 16ms (Beats 85.71%)
 • Memory: 12.61MB (Beats 73.13%)

