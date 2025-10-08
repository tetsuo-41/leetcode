# 🧩 問題名: [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

## 📝 問題概要

2つの文字列 `text1`, `text2` が与えられる。  
両方の文字列に共通する **最長の部分列 (Longest Common Subsequence, LCS)** の長さを求めよ。  

部分列とは、文字を削除しても構わないが、**残った文字の順序は変えない**文字列のこと。  

### 🔍 例

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: 共通部分列は "ace"

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: 共通部分列は "abc"

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: 共通部分列は存在しない


---

## ✅ 解法方針（Approach）

### 💡 コアアイデア：動的計画法（Dynamic Programming, DP）

この問題は「過去の結果をもとに次の結果を決める」構造を持つため、DPを使うのが定石。  
`dp[i][j]` を「`text1` の最初の `i` 文字と `text2` の最初の `j` 文字のLCSの長さ」と定義する。

---

### 🧩 遷移式（状態遷移）

1. **文字が一致する場合**  
text1[i-1] == text2[j-1]
→ dp[i][j] = dp[i-1][j-1] + 1
→ 共通部分列を1文字延ばせる。

2. **文字が一致しない場合**  
text1[i-1] != text2[j-1]
→ dp[i][j] = max(dp[i-1][j], dp[i][j-1])
→ 一方の文字を削除して、長い方を選ぶ。

---

### 🧱 初期条件

- `dp[0][*] = dp[*][0] = 0`  
（空文字とのLCSは0）

---

### 🧠 図解イメージ（例: text1="abcde", text2="ace"）

|   |   | a | c | e |
|---|---|---|---|---|
|   | 0 | 0 | 0 | 0 |
| a | 0 | 1 | 1 | 1 |
| b | 0 | 1 | 1 | 1 |
| c | 0 | 1 | 2 | 2 |
| d | 0 | 1 | 2 | 2 |
| e | 0 | 1 | 2 | 3 |

最終結果 `dp[-1][-1] = 3`

---

## ⏱️ 計算量

- **時間計算量:** O(m × n)  
（`m = len(text1)`, `n = len(text2)`）  
2重ループで全ての組み合わせを計算。イチから総当たりで計算するとO(2^n)

- **空間計算量:** O(m × n)  
DPテーブルのサイズ分のメモリを使用。

※ さらに最適化するなら、行ごとに更新して **O(min(m, n))** にもできる。

---

## 🧠 ポイントと学び

- LCSはDPの代表的問題であり、「2次元DPの基礎」。
- 部分列（subsequence）と部分文字列（substring）の違いに注意。
- 一致しないときに `max(dp[i-1][j], dp[i][j-1])` を取るのが肝。

---

## 📈 提出結果（例）

- Runtime: **527ms** (Beats 74.00%)  
- Memory: **33.56MB** (Beats 74.44%)

---