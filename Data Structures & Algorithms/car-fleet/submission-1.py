class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = sorted(zip(position, speed), reverse=True)

        for car in cars:
            pos,spe = car
            arr = (target - pos) / spe
            if stack:
                pos,spe = stack[-1]
                arr2 = (target - pos) / spe
                if arr > arr2:
                    stack.append(car)
            else:
                stack.append(car)

        return len(stack)