class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        self.result = []

        def backtrack(index, current):
            if index == len(digits):
                self.result.append(current.copy())
                return 

            for i in hashmap[digits[index]]:
                backtrack(index+1, current)