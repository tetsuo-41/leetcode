# 🧩 問題名: [139. Word Break]

## 📝 問題概要

文字列 `s` と、単語の辞書 `wordDict` が与えられる。
wordDict に含まれる単語を使って、s を空白で区切って構成できるかを判定せよ。
同じ単語を複数回使っても良い。

## 🔍 例

### Example 1
Input: `s = "leetcode", wordDict = ["leet", "code"]`
Output: `true`
Explanation: "leet code" に分割できる。

### Example 2
Input: s = `"applepenapple", wordDict = ["apple", "pen"]`
Output: `true`
Explanation: `"apple pen apple"` に分割できる。

### Example 3
Input: `s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]`
Output: `false`

## ✅ 解法方針（Approach）

### 💡 コアアイデア:Dynamic Programming
-動的計画法（DP）を使用して、`s[0:i]` までが辞書の単語で構成可能かどうかを `dp[i]` に記録する。
-例えば、`dp[3] = True` なら、`s[0:3]` は構成可能という意味。
-`s[j:i]` が辞書にあり、かつ `dp[j] == True` なら、`dp[i]` も `True` とできる。

## 🧠 高速化テクニック

wordDict を set に変換して高速な検索`（O(1))` を可能にする。

辞書内の最大単語長 `max_len` を使って、`s[j:i]` の長さが max_len を超えるものはスキップ。
→ 無駄な部分文字列の探索を省略。

## ⏱️ 計算量

時間計算量: `O(n * m)`
（n は文字列長、m は最大単語長。内側ループを max_len に制限することで高速化）

空間計算量: `O(n)`（dpテーブル使用）

## 🧠 ポイントと学び
- DPにおいて「区切り位置」を内側ループで探すのが典型パターン。
- s[0:i] が条件を満たすかを1文字ずつ確認するような処理は、スライディングウィンドウ的な視点をもてると強い。
- 単語辞書が与えられる場合は、setにして O(1) 検索にするのが基本。

## 📈 提出結果
• Runtime: 0 ms (Beats 100.00%)
• Memory: 12.54 MB (Beats 42.00%)