class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        

        def dfs(index,node):
                
            if index == len(word):
                return node.end
            
            c = word[index]  
            
            if c == ".":
                for child in node.children.values():
                    if dfs(index+1, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(index+1, node.children[c])
        return dfs(0,self.root)

        

