class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        queue = deque()  # (count, available_at)
        time = 0

        while heap or queue:
            time += 1

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

            if heap:
                cnt = heapq.heappop(heap) + 1  # +1 weil negativ
                if cnt:  # noch Tasks übrig
                    queue.append((cnt, time + n + 1))

        return time