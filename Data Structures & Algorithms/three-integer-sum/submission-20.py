class Solution:
      def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        i = 0
        print(nums)
        while i < len(nums)-2:
            
            l = i + 1
            r = len(nums) - 1
            print(i,l,r)
            while l < r:
                add = nums[r] + nums[l] + nums[i]
                if add == 0:
                    sol.append([nums[r],nums[l],nums[i]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                elif add > 0:
                        r -= 1
                else:
                        l += 1
            while nums[i] == nums[i+1] and i < len(nums)-2:
                i += 1
            i += 1
            
        return sol
                    
            