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
        n = len(cost)

        if sum(gas) - sum(cost) < 0:
            return -1

        tank = 0
        i = 0
        while i < n:
            tank = 0
            for j in range(i,i+n+1):
                if j == n:
                    return i
                tank += gas[j] - cost[j]
                if tank < 0:
                    break
            i = j + 1

            

