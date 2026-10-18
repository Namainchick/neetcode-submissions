class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def backtrack(index, state):
            if (index, state) in dp:                  # Schlüssel = ganzer Zustand
                return dp[(index, state)]

            if index == len(s):                       # == statt >
                return 1 if state == -1 else 0        # offene Zweierzahl = ungültig

            d = int(s[index])                         # Ziffer als Zahl
            if state == 2:                            # vorher '2': nur 20..26
                sol = backtrack(index + 1, -1) if d <= 6 else 0
            elif state == 1:                          # vorher '1': 10..19 geht immer
                sol = backtrack(index + 1, -1)
            elif d == 0:                              # einzelne 0 hat keinen Buchstaben
                sol = 0
            elif d == 1:
                sol = backtrack(index + 1, 1) + backtrack(index + 1, -1)
            elif d == 2:
                sol = backtrack(index + 1, 2) + backtrack(index + 1, -1)
            else:                                     # 3..9: nur einzeln
                sol = backtrack(index + 1, -1)

            dp[(index, state)] = sol                  # einmal speichern statt in jedem Zweig
            return sol

        return backtrack(0, -1)
