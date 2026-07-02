class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        self.children = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTree()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in self.children:
                return False
            node = node.children[c]
        if node.isEnd:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for c in prefix:
            if c not in self.children:
                return False
            node = node.children[c]
        return True
        