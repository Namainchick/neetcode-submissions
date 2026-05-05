class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict()
        sol = []

        for s in strs:
            chars = tuple(sorted(s))
            if not chars in hash:
                hash[chars] = [s]
            else:
                hash[chars].append(s)
            
        for s in hash:
            sol.append(hash[s])

        return sol

            