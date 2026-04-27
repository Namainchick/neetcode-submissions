class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for i,s in enumerate(strs):
            hash[self.counter(s)].append(s)
        ans = []
        for i in hash:
            ans.append(hash.get(i))
        return ans
    def counter(self, string: str):
        counts = [0] * 26
        for c in string:
            counts[ord(c) - ord('a')] += 1
        return tuple(counts)
