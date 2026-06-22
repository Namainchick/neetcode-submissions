class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for i in counter:
            if counter[i] >= 2:
                return True
        return False         