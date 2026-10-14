class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.result = []
        self.adj = defaultdict(list)

        for f,t in tickets:
            self.adj[f].append(t)

        def backtrack(current):
            if len(current) == len(tickets) + 1:
                self.result = current.copy()
                return 
            cur = current[len(current)-1]
            for nei in self.adj[cur]:
                current.append(nei)
                self.adj[cur].remove(nei)
                backtrack(current)
                current.pop()
                self.adj[cur].append(nei)

        for f,t in tickets:
            backtrack([f])

        return self.result 


        