class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            min_len = min(len(w1),len(w2))
            if len(w2) < len(w1) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        result = []

        def dfs(node):
            if node in visited:
                return visited[node]

            visited[node] = True

            for nei in adj[node]:
                if dfs(nei):
                    return True
            
            result.append(node)
            visited[node] = False

        for c in adj:
            if dfs(c):
                return ""

        result.reverse()

        return "".join(result) 
