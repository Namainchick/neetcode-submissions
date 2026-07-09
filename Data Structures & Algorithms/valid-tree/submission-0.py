class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        neighbours = defaultdict(list)
        for a,b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        visited = set()
        
        def dfs(node):
            visited.add(node)
            for neighbour in neighbours[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        dfs(0)
        return len(visited) == n