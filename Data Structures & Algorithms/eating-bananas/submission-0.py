class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        best = float('inf')
        s = 0
        greatest = 0

        for i in piles:
            s += i
            greatest = max(greatest,i)

        l = 1
        r = greatest

        while l <= r:
            mid = (l + r) // 2
            sol = 0
            for i in piles:
                sol += (i+mid-1) // mid
            if sol <= h:
                best = mid
                r = mid - 1 
            else:
                l = mid + 1
        return best

