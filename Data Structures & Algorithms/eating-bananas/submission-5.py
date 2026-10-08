class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h
        l,r = 1,max(piles)

        def check_eat(rate):
            counter = 0
            for i in self.piles:
                counter +=  math.ceil(i/rate)

                if counter > self.h:
                    return False
            return True

        while l <= r:
            mid = (l+r) // 2
            if check_eat(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l