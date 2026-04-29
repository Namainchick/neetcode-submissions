class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        if len(nums) == 3 and (nums[0] + nums[1] + nums[2]) == 0:
            return [[0,0,0]]
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            print(i)
            while l < r:
                while l<r and nums[l+1] == nums[l]:
                    l += 1 
                while l<r and nums[r-1] == nums[r]:
                    r -= 1 
                sum = nums[l] + nums[r] + nums[i]
                if sum == 0:
                    sol.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif sum < 0:
                    l += 1 
                else:
                    r -= 1 
        return sol

            