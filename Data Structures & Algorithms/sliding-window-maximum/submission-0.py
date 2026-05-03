class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()

        l = 0

        res = []
        for r in range(len(nums)):
            if not d:
                d.append(r)
            while d and nums[d[-1]] < nums[r]:
                d.pop()
                d.append(r)
            if r-l+1 == k:
                print(l,r)
                while d[0] not in range(l,r+1):
                    d.popleft()
                res.append(nums[d[0]])
                l += 1
        return res

