"""
1. step: building the tree out of the possible words
2. smartly go through the board to see if word can be build
"""
class Node():
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = []
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.root = Node()

        row = len(board)
        col = len(board[0])

        for word in words:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.end = True

        def dfs(i,j,node,current):
            c = board[i][j]
            board[i][j] = "#"
            current.append(c)

            if c in node.children:
                node = node.children[c]
                if node.end:
                    self.result.append("".join(current))
                    node.end = False
                for x,y in self.directions:
                    if 0 <= i+x <= row-1 and 0 <= j+y <= col-1 and board[i+x][j+y] != "#":
                        dfs(i+x,j+y,node,current)

            current.pop()
            board[i][j] = c

        for i in range(row):
            for j in range(col):
                dfs(i,j,self.root,[])
        
        return self.result
                    
        
