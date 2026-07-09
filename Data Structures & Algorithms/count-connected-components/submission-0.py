class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == n-1:
            return 1

        neighbours = defaultdict(list)
        for a,b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        counter = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbour in neighbours[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        for i in range(n):
            if i not in visited:
                dfs(i)
                counter += 1
        return counter

