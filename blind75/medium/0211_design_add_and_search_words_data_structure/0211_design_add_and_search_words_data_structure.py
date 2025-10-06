# LeetCode 211. Design Add and Search Words Data Structure
# Difficulty: Medium
# Runtime: 2697ms, Beats 60.95%/ Memory: 117.13MB, Beats 44.45%


class TrieNode:
    def __init__(self):
        self.children = {}  # 子ノード
        self.is_end = False # 単語終端フラグ

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            char = word[i]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
        
        return dfs(self.root, 0)

# 使用例
# obj = WordDictionary()
# obj.addWord("bad")
# param_2 = obj.search("b..") # True
