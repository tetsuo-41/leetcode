# LeetCode 208. Implement Trie (Prefix Tree)
# Difficulty: Medium
# Runtime: 74ms, Beats 78.23%/ Memory: 39.09MB, Beats 42.95%

class TrieNode:
    def __init__(self):
        self.children = {}  # 子ノードを格納する辞書
        self.is_end = False # 単語の終端かどうかを示すフラグ

class Trie(object):

    def __init__(self):
        self.root = TrieNode()  # ルートノードを初期化

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True  # 単語の終端をマーク

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end  # 終端フラグがTrueなら単語が存在

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True  # prefixの探索が全て成功すればOK

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)