# brute force going through all solutions: 2^n
# better would be either skipping or searching smartly
# in this case idk lets try brute force 

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.zeros = defaultdict(int)
        self.ones = defaultdict(int)
        self.result = 0

        for s in strs:
            for i in s:
                if i == "0":
                    self.zeros[s] += 1
                else:
                    self.ones[s] += 1
        
        def backtrack(start, path):
            one,zero = 0,0
            for s in path:
                one += self.ones[s]
                zero += self.zeros[s]

            if zero <= m and one <= n:
                self.result = max(self.result,len(path))
                
            for i in range(start, len(strs)):
                path.append(strs[i])        
                backtrack(i + 1, path)      
                path.pop()
        
        backtrack(0, [])
    
        return self.result
