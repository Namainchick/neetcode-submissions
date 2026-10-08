class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h

        def check_eat(rate):
            counter = 0
            for i in self.piles:
                while i > 0:
                    counter += 1
                    i -= rate 

                if counter > self.h:
                    return False
            return True
                
        
        l,r = 0,max(piles)

        while l <= r:
            mid = (l+r) // 2
            if check_eat(mid):
                r = mid - 1
            else:
                l = mid + 1

        return r