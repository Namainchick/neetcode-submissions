class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        l = 0 
        r = m

        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i

            l1 = nums1[i-1] if i > 0 else float('-inf')
            r1 = nums1[i] if i < m else float('inf')
            l2 = nums2[j-1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)

            if l1 > r2:
                r = i - 1
            else:
                l = i + 1
