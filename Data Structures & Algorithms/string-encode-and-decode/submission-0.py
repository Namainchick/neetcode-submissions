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
            if s[index] in self.valid:
                num = num + s[index]
            elif s[index] == "#":
                gap = int(num) + 1
                ans.append(s[index+1:index+gap])
            index += 1
        return ans