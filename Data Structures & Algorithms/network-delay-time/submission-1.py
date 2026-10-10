class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = [0] * (n + 1)
        visited = set()
        pre = {}
        self.possible = True

        for u,v,t in times:
            if v not in pre:
                pre[v] = []
            pre[v].append((u,t))

        def dfs(node):
            if node == k:
                return True

            result = False

            if node not in pre[v]:
                return False
            else:
                best = float('inf')
                for pv,t in pre[v]:
                    if time[pv] == 0:
                        if dfs(pv):
                            result = True
                best = min(best,time[pv]+t)

                time[node] = best 

            return result

        
        for node in range(1,n+1):
            if time[node] == 0:
                if not dfs(node):
                    return -1
        print(time)
        return max(time)
        



        