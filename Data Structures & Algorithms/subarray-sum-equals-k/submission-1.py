class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        sum_count = {0:1}
        cur_sum = 0


        for n in nums:
            cur_sum += n
            result += sum_count.get(cur_sum-k,0)
            sum_count[cur_sum] = sum_count.get(cur_sum,0) + 1

        return result