# 🧩 問題名: [449. Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/)

## 📝 問題概要

二分探索木（BST）が与えられる。  

- **serialize**：BST を文字列に変換  
- **deserialize**：その文字列から元の BST に復元  

どのような方法で変換してもよいが、**できるだけコンパクトにすること**が推奨されている。  

### 🔍 例
Input: root = [2,1,3]  
Output: [2,1,3]  

Input: root = []  
Output: []  

制約:  
- ノード数は 0 ～ 10⁴  
- ノード値は 0 ～ 10⁴  
- 入力は必ず BST  

## ✅ 解法方針（Approach）

### 💡 コアアイデア
- BST の特性を活かす  
  - **左の子 < 親 < 右の子**  
  - preorder（根 → 左 → 右）で serialize すれば、復元時に範囲制約で簡単に復元できる
- 文字列化の際は、数値をカンマでつなぐだけで十分
- deserialize 時は preorder 配列を順に見ながら BST を再構築

---

## ⏱️ 計算量
- 時間計算量: O(n)
各ノードは preorder で 1 回だけ処理
- 空間計算量: O(n)
preorder 配列と再帰スタック分

## 🧠 ポイントと学び
- 「BST は preorder を使えば 値の範囲制約だけで復元可能
- deserialize の際に min_val と max_val を使うことで、左か右かを簡単に判定できる
- serialize は「値だけ記録する」というシンプルな方法で十分コンパクト
---

## 📈 提出結果
- Runtime: 46ms (Beats 94.20%)  
- Memory: 20.32MB (Beats 62.32%)  

---

