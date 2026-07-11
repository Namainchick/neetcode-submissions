class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x 

        def union(a,b):
            a,b = find(a),find(b)
            if a == b:
                return False
            parent[a] = b
            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]