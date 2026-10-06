class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        
        [2,-1,1,2]
        [2, 1,2,3]

        """

        preSum = [0]
        result = 0

        for n in nums:
            if not preSum:
                preSum.append(n)
            else:
                preSum.append(preSum[-1]+n)

        for i in range(len(nums)+1):
            for j in range(len(nums)+1):
                if preSum[j] - preSum[i] == k:
                    result += 1
        
        return result