class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h

        def check_eat(self,rate):
            counter = 0
            for i in pile:
                counter +=  math.ceil(i/rate)
            return True
                
        
        l,r = 0,max(piles)

        while l <= r:
            mid = (l+r) // 2
            if check_eat(mid):
                r = mid - 1
            else:
                l = mid + 1