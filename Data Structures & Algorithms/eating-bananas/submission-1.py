class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        best = float('inf')
        greatest = max(piles)

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

#had problems finding the ceiling of a number the rest went pretty smothely binary search is just the same in every problem till now

