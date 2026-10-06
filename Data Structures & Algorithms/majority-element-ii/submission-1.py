class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,5,2,5,3,2,2,2,3]

        - 2 2 2 2 
        - 5
        - 3 3 

        """

        n = len(nums) // 3

        result = []

        first = 0
        f_count = 0
        second = 0
        s_count = 0
        third = 0
        t_count = 0

        for i in nums:
            min_count = min(f_count,s_count,t_count)

            if i in (first,second,third):
                if first == i:
                    f_count += 1
                elif second == i:
                    s_count += 1
                elif third == i:
                    t_count += 1

            elif min_count == 0:
                if f_count == 0:
                    first = i
                    f_count = 1
                elif s_count == 0:
                    second = i
                    s_count = 1
                elif t_count == 0:
                    third = i
                    t_count = 1

            else:
                f_count -= 1
                s_count -= 1
                t_count -= 1

        f_count,s_count,t_count = (0,0,0)

        for i in nums:
            if i == first:
                f_count += 1
            if i == second:
                s_count += 1
            if i == third:
                t_count += 1

        if f_count > n:
            result.append(first)
        if s_count > n:
            result.append(second)
        if t_count > n:
            result.append(third)

        return result