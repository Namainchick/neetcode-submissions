class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_counter = {
            5: 0,
            10:0,
            20:0
        }

        def pay(amount):

            while amount >= 20 and bill_counter[20] > 0:
                bill_counter[20] -= 1
                amount -= 20
            while amount >= 10 and bill_counter[10] > 0:
                bill_counter[10] -= 1
                amount -= 10
            while amount >= 5 and bill_counter[5] > 0:
                bill_counter[5] -= 1
                amount -= 5

            return amount == 0

        for bill in bills:
            if not pay(bill-5):
                return False
            bill_counter[bill] += 1

        return True
