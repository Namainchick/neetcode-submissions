class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        nxt1,nxt2  = 0,0
        for x in reversed(nums[1:]):
            nxt1,nxt2 = max(nxt1,nxt2+x),nxt1

        result = nxt1

        nxt1,nxt2  = 0,0
        for x in nums[:n-1]:
            nxt1,nxt2 = max(nxt1,nxt2+x),nxt1

        return max(result,nxt1)