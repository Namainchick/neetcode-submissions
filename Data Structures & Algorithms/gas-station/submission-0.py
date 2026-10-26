class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        we start in the beginning and see how far we can get. If we stop somewhere we know that in 
        that range we can never start. Because getting to the next it means your cost needs to be 
        neutral or positive. Now thinking that we can start in the middle of a broken way we need 
        to assume that somwhere before that it was stronlgy negative which is impossible becuase if 
        yes you would never reach that middle. 
        We end if a try end in the range that we know doesnt work. 
        """

        i = 0
        tank = 0
        n = len(gas)

        while i < n:
            tank = 0
            j = 0
            for j in range(i,i+n+1):
                k = j
                if j >= n:
                    k = j - n
                tank += gas[k] - cost[k]
                if tank < 0:
                    break
            if j == n+i:
                return i
            else:
                i = j+1

        return -1
            

