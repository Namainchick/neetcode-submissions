class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        hashmap = Counter(nums)

        for i in range(hashmap[val]):
            nums.remove(val)

        return len(nums)
