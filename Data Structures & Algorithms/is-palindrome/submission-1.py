class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        k = "".join(c for c in s.lower() if c.isalnum())
        l = 0
        r = len(k)-1
        print(k)
        while l < r:
            print(k[l],k[r])
            if k[l] == k[r]:
                l+=1
                r-=1
            else:
                return False
        return True