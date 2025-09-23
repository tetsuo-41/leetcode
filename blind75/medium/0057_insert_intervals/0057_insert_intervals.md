# 🧩 問題名: [57. Insert Interval](https://leetcode.com/problems/insert-interval/)

## 📝 問題概要

**非重複・昇順にソートされた区間の配列 `intervals`** と、追加する区間 `newInterval` が与えられる。  

- 各区間は `[start, end]` で表される。
- `newInterval` を `intervals` に挿入しつつ、**重なりがあればマージする**。  
- 最終的に **重複のない昇順ソート済み区間** の配列を返す。

### 🔍 例
**例1**  
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]  
Output: [[1,5],[6,9]]  
Explanation: [2,5] は [1,3] と重なるのでマージ → [1,5]  

**例2**  
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]  
Output: [[1,2],[3,10],[12,16]]  
Explanation: [4,8] は [3,5],[6,7],[8,10] と重なる → マージして [3,10]  

## ✅ 解法方針（Approach）

### 💡 コアアイデア
1. **新しい配列 `res`** を作り、マージ済み区間を追加していく。
2. `newInterval` より **前に重ならない区間** はそのまま `res` に追加。
3. **重なる区間** は `newInterval` とマージして更新。  
   - 新しい `newInterval` = `[min(start1, start2), max(end1, end2)]`
4. **新しい区間が終わった後の区間** は残りの区間を順に `res` に追加。
5. 最終的に `res` が結果。

### 🧠 マージの判断
- `interval[1] < newInterval[0]` → 完全に前 → そのまま追加  
- `interval[0] > newInterval[1]` → 完全に後 → newInterval を追加後、残りも追加  
- 上記以外 → 重なっている → マージして newInterval を更新  

## ⏱️ 計算量
- **時間計算量**: O(n)  
  - 各区間を1回ずつ見るだけでマージできる  
- **空間計算量**: O(n)  
  - 新しい配列 `res` を使用

## 🧠 ポイントと学び
- 区間マージ系の典型問題  
- 「重なり」の判定を `interval[1] < newInterval[0]` / `interval[0] > newInterval[1]` で考えるとスッキリ
- 挿入位置に関わらず1回のループで解ける

---

## 📈 提出結果
- Runtime: 3ms (Beats 56.11%)  
- Memory: 14.29MB (Beats 48.57%)  

---
