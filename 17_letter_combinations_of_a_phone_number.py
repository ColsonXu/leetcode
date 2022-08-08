class Solution:
    def letterCombinations(self, digits):
        keys = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
        }

        res = []

        def backtrack(i, comb):
            if len(comb) == len(digits):
                res.append(comb)
                return

            for char in keys[digits[i]]:
                backtrack(i + 1, comb + char)

        if digits:
            backtrack(0, "")

        return res
