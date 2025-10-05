# 🧩 問題名: [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

## 📝 問題概要

Trie（トライ）または Prefix Tree は、文字列の集合を効率的に格納・検索するためのデータ構造である。  
この問題では、以下の 3 つの主要な操作を実装する：

1. `insert(word)`：文字列 `word` を Trie に挿入する  
2. `search(word)`：`word` が Trie に完全一致して存在するか判定  
3. `startsWith(prefix)`：`prefix` で始まる単語が Trie に存在するか判定  

---

### 🔍 例

```python
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output:
[null, null, true, false, true, null, true]

Explanation:
trie = Trie()
trie.insert("apple")
trie.search("apple")   # True
trie.search("app")     # False
trie.startsWith("app") # True
trie.insert("app")
trie.search("app")     # True
```

## ✅ 解法方針（Approach）

### 💡 コアアイデア
- Trie は木構造を使い、各ノードは次の文字への参照（子ノード）を持つ。
- ノードには文字自体ではなく、子ノードへの辞書を持たせるのが簡単。
- また、そのノードが単語の終わりかどうかを示すフラグ isEnd を持つ。

---

## 🧠 各操作の考え方
### 1 insert(word)
- 先頭から順に文字を辿り、存在しなければ新しいノードを作成。
- 最後の文字のノードに isEnd = True をセット。
### 2 search(word)
- 文字を順に辿る。
- 途中で存在しない文字があれば False。
- 最後の文字に到達したら isEnd が True か確認。
### 3 startsWith(prefix)
- search と同じだが、最後の文字で isEnd は問わずに到達できれば True。

## ⏱️ 計算量
- 時間計算量: O(L)（L = 単語の長さ）
- 空間計算量: O(N * L)（N = 単語数）

---

## 🧠 ポイントと学び
- Trie は 共通接頭辞をまとめて管理できるため、文字列検索の効率が高い。
- search と startsWith の違いは、最後のノードで is_end を確認するかどうか。
- オートコンプリート・スペルチェックなどに応用可能。

---

### 📈 提出結果
- Runtime: 74ms (Beats 78.23%)  
- Memory: 39.09MB (Beats 42.95%)  

---