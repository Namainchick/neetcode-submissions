class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0,len(arr)-1
        res = []

        while l <= r:
            mid = (l+r) // 2
            if arr[mid] <= x:
                l = mid + 1
            else:
                r = mid - 1 

        if r == -1:
            r = 0
            l = 1

        print(r)

        counter = 0

        while counter != k and r >= 0 and l < len(arr):
            if abs(arr[r]-x ) > abs(arr[l]-x):
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r -= 1

            counter += 1

        while counter != k and r >= 0:
            res.append(arr[r])
            r -= 1

            counter += 1

        while counter != k and l < len(arr):
            res.append(arr[l])
            l += 1

            counter += 1
            
        res.sort()
        return res
