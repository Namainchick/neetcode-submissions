class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque()
        adj = defaultdict(list)
        for f, t, p in flights:
            adj[f].append((t, p))

        result = float('inf')

        q.append((src,0,0))
        
        while q:
            port,step,price = q.popleft()
            
            if step == k+1:
                if port == dst:
                    result = min(price,result)
                continue

            if port == dst:
                result = min(price,result) 
                continue

            for nei_port,nei_price in adj[port]:
                q.append((nei_port,step+1,nei_price+price))

        return result if result != float('inf') else -1