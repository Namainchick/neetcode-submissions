class Solution:
    valid = "0123456789"
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            l = len(s)
            ans = ans + str(l) + "#" + s
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        index = 0
        num = ""
        while index < len(s):
            if s[index] == "#":
                length = int(num)
                ans.append(s[index+1 : index+1+length])
                index = index + 1 + length    # spring direkt zur nächsten Länge
                num = ""                       # reset!
            else:
                num += s[index]
                index += 1
            
        return ans