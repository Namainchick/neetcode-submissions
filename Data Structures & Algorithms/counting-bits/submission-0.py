class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        this has to be a math problem 
        """ 
        out = [0] * (n+1)
        power = 1

        for i in range(1, n+1):
            if i == power * 2:
                power *= 2
            
            out[i] = out[i - power] + 1

        return out
