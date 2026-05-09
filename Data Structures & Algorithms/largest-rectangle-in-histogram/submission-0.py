class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # enthält (start_index, höhe)
        best = 0
        
        for i in range(len(heights) + 1):
            # am Ende tun wir so, als wäre die Höhe 0
            curr_height = heights[i] if i < len(heights) else 0
            start = i
            
            while stack and stack[-1][1] > curr_height:
                s, h = stack.pop()
                area = (i - s) * h
                best = max(best, area)
                start = s  # neuer Balken erbt den Start
            
            stack.append((start, curr_height))
        
        return best