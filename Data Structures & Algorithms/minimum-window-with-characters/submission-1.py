class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
              return ""

        current = 0
        window = defaultdict(int)
        need = Counter(t)
        required = len(need)
        best = ""
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if window[c] == need[c]:
                current += 1

            while current == required:
                print(best)
                if not best or r-l+1 < len(best):
                    best = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    current -= 1
                l += 1
        return best