class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.result = []
        self.adj = defaultdict(list)
        tickets.sort()

        for f,t in tickets:
            self.adj[f].append(t)

        self.result = ["JFK"]

        def backtrack():
            if len(self.result) == len(tickets) + 1:
                return True
            
            cur = self.result[-1]
            for i in range(len(self.adj[cur])):
                nei = self.adj[cur][i]
                if nei is None:
                    continue
                self.adj[cur][i] = None
                self.result.append(nei)
                if backtrack():
                    return True
                self.result.pop()
                self.adj[cur][i] = nei
            return False

        backtrack()
        return self.result


        