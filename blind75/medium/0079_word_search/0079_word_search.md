# 🧩 問題名: [79. Word Search](https://leetcode.com/problems/word-search/)

## 📝 問題概要

m x n の文字グリッド `board` と文字列 `word` が与えられる。  
`board` 内の文字を使って `word` を作れる場合は `True` を返す。  

**制約条件**  
- 文字は水平方向または垂直方向に隣接するセルから順番に選ぶ  
- 同じセルを複数回使うことはできない  

### 🔍 例

**Example 1**  
Input:  
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"  
Output: True  
Explanation: A→B→C→C→E→D と辿れる  

**Example 2**  
Input:  
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "SEE"  
Output: True  

**Example 3**  
Input:  
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCB"  
Output: False  

## ✅ 解法方針（Approach）

### 💡 コアアイデア
- DFS（深さ優先探索）＋バックトラックで解く  
- board の各セルをスタート地点として、word の各文字を順に探索  
- 移動は上下左右のみ  
- 探索中に訪れたセルは再利用できないので、一時的にマークして探索終了後に戻す（バックトラック）

### 🧠 具体的な手順
1. board の全セルをループで回す  
2. そのセルの文字が word の先頭と一致すれば DFS を開始  
3. DFS 内で以下を実施:  
   - 現在のセルの文字が word の現在位置と一致しなければ False を返す  
   - word が最後まで到達すれば True を返す  
   - 上下左右の隣接セルに対して再帰 DFS を行う  
   - 探索終了後にセルを元に戻す（バックトラック）

### ⏱️ 計算量
- 時間計算量: O(m * n * 4^L)  
- 空間計算量: O(L)（再帰呼び出しスタック）

## 🧠 ポイントと学び
- DFS＋バックトラックは「探索と戻す」をセットで考える  
- 「同じセルは1回しか使えない」という制約は一時的なマークで簡単に実装可能  
- 小さいグリッド（m,n <= 6）なら 4^L の探索も許容範囲

## 📈 提出結果
- Runtime: 5426ms (Beats 86.69%)  
- Memory: 12.49MB (Beats 52.47%)
