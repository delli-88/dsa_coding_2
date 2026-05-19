class Solution:

    def partition(self, s):
        sol = []
        self.helper(s, 0, [], sol)
        return sol

    def helper(self, s, pos, subset, sol):

        if pos == len(s):
            sol.append(subset[:])
            return

        for end in range(pos, len(s)):
            curr = s[pos:end+1]

            if self.isPalindrome(curr):
                subset.append(curr)
                self.helper(s, end+1, subset, sol)
                subset.pop()

    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

print(Solution().partition(s = "aab"))