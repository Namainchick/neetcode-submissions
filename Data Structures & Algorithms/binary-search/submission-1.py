class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        return r if nums[r] == target else -1

#i know how to do binary searh but i had prolem implementing and keeping track of the indexes i would put it in mid level hard 
            
