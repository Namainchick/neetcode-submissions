class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        index = 0
        for i in arr:
            if count[i] == 1:
                index += 1
            if index == k:
                return i
        return ""