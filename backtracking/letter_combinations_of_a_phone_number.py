class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        digitsMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        self.backtrack(0, [], digits, digitsMap, result)
        return result

    def backtrack(self, pos, path, digits, digitsMap, result):
        if pos == len(digits):
            result.append("".join(path))
            return

        for ch in digitsMap[digits[pos]]:
            path.append(ch)
            self.backtrack(pos + 1, path, digits, digitsMap, result)
            path.pop()
        
        return

print(Solution().letterCombinations(digits = "23"))