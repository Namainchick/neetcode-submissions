class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        best = 0
        for i in nums:
            if i - 1 in hash:
                continue
            length = 1
            while i + length in hash:
                length += 1
            best = max(best,length)

        return best
