class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l = 0 
        r = 0
        n = len(height)
        while l < n-1 and r < n-1:
            if height[l] == 0 and height[r] == 0:
                l += 1
                r += 1
            else:
                r += 1 
                highest = r
                while height[r] < height[l] and r<n-1:
                    r += 1
                    highest = highest if height[highest] > height[r] else r
                if r == n-1 and r != highest:
                    r = highest
                if r-l > 1:
                    pot = min(height[l],height[r])*(r-l-1)
                    print(pot,r,l)
                    for i in range(l+1,r):
                        pot -= height[i]
                    print(pot)
                    area += pot
                l = r 
        return area
            