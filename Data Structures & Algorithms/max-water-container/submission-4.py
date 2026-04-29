class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0 
        r = len(heights) - 1 

        while l<r:
            vol = (r - l)*min(heights[r],heights[l])
            best = max(vol,best)
            print(r,l)
            if heights[r]<heights[l]:
                r -= 1
            elif heights[r]>heights[l]:
                l += 1
            else:
                l += 1
                r -=1 
        return best
