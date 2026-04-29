class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0 
        r = len(heights) - 1 

        while l<r:
            vol = (r - l)*min(heights[r],heights[l])
            best = max(vol,best)
            if r<l:
                r -= 1
            elif r>l:
                l += 1
            else:
                break
        return best
