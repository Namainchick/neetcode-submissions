class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)

        if s % 2 != 0:
            return False

        seen = set()
        seen.add(0)

        for num in nums:
            for cur in list(seen):
                if cur + num == s / 2:
                    return True
                elif cur + num not in seen and cur + num < s / 2:
                    seen.add(cur+num)

        return False
        