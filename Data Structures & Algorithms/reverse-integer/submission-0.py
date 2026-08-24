class Solution:
    def reverse(self, x: int) -> int:
        sign = False
        if x < 0:
            sign = True
        
        out =  int(str(abs(x))[::-1]) if not sign else int(str(abs(x))[::-1]) * -1
        if out <= -2**31 or out >= 2**31:
            return 0
        return out