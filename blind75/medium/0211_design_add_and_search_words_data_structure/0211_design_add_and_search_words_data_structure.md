# 🧩 問題名: [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)


## 📝 問題概要

単語を追加したり、検索できるデータ構造を設計せよ。  
検索文字列には「`.`」を含めることができ、`.` は任意の1文字にマッチする。

実装するクラス:

- `WordDictionary()` : 初期化
- `addWord(word)` : 単語を追加
- `search(word)` : 文字列が追加済みの単語にマッチするか返す（`.` を含む可能性あり）

---

### 🔍 例
```python
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output:
[null,null,null,null,false,true,true,true]

Explanation:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad") # False
wordDictionary.search("bad") # True
wordDictionary.search(".ad") # True
wordDictionary.search("b..") # True
```
---

## ✅ 解法方針（Approach）

### 💡 コアアイデア

- 「単語を管理するデータ構造」として Trie（Prefix Tree） を用いる。
- Trieノードには子ノードの辞書 (children) と単語終端フラグ (is_end) を持たせる。
- 単語の追加 (addWord) は普通のTrieと同じで、文字を順に辿りノードを作る。
- 検索 (search) では文字が . の場合、すべての子ノードを再帰的に探索する。
- 文字が通常文字なら該当子ノードに進む。
- 最終文字まで到達したら is_end を確認してマッチ判定。

---

### 🧠 ドット . の扱い
- ドットが出現した場合、全ての子ノードを探索する必要がある。
- 2つ以下しかない制約なので再帰的DFSで十分。

---

## ⏱️ 計算量
- addWord(word) : O(L)
  - （L は単語の長さ）
- search(word) : 最悪 O(26^M)
  - （M はドットの数。制約で最大2なので現実的に高速）
- 空間計算量: O(N * L)
  - （追加した単語数 N と平均長さ L）

---

## 🧠 ポイントと学び
- Trie は部分一致検索やワイルドカード検索に強い。
- 「. は何にでもマッチ」という特性は DFSで枝刈り することで効率的に実装可能。
- 制約により再帰で十分だが、無制限のドットだと工夫が必要。

---

### 📈 提出結果
- Runtime: 2697ms (Beats 60.95%)  
- Memory: 117.13MB (Beats 44.45%)  

---