class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        best = ""
        shortest = float('inf')

        for i in strs:
            shortest = min(shortest,len(i))
        
        for index in range(shortest):
            c = ""
            over = False
            for s in strs:
                if not c:
                    c = s[index]
                elif c != s[index]:
                    over = True
                    break
            if over:
                break
            best = best + c
        return best