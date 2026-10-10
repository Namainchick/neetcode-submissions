class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        result = 0
        heap = []
        adj = defaultdict(list)

        for u,v,t in times:
            adj[u].append((v,t))

        heap.append((0,k))

        while heap:
            time,node = heapq.heappop(heap)
            if node in visited:
                break
            result = max(result,time)
            for target,target_time in adj[node]:
                if target not in visited:
                    heapq.heappush(heap,(time+target_time,target))

            visited.add(node)

        return result if len(visited) == n else -1
            
        



        