class Solution:
      def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        i = 0
        print(nums)
        while i < len(nums)-2:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                add = nums[i] + nums[l] + nums[r]
                if add == 0:
                    sol.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif add > 0:
                    r -= 1
                else:
                    l += 1
            while i < len(nums)-2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
            
        return sol
                    
            