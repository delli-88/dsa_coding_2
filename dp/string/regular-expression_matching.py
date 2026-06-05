class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1 for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        return self.helper(s, p, 0, 0, dp)

    def helper(self, s, p, pos1, pos2, dp):

        # Pattern finished
        if pos2 == len(p):
            return pos1 == len(s)
        
        if dp[pos1][pos2] !=-1:
            return dp[pos1][pos2]

        # Does current character match?
        first_match = (
            pos1 < len(s)
            and (s[pos1] == p[pos2] or p[pos2] == '.')
        )

        # Case: next pattern character is '*'
        if pos2 + 1 < len(p) and p[pos2 + 1] == "*":

            # Option 1: ignore x*
            skip_star = self.helper(s, p, pos1, pos2 + 2, dp)

            # Option 2: use x* to consume one character
            use_star = first_match and self.helper(s, p, pos1 + 1, pos2, dp)

            dp[pos1][pos2] = skip_star or use_star
            return dp[pos1][pos2] 

        # Normal character match
        dp[pos1][pos2] = first_match and self.helper(s, p, pos1 + 1, pos2 + 1, dp)
        return dp[pos1][pos2]

    def isMatchTabulization(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case
        dp[m][n] = True

        for pos1 in range(m, -1, -1):
            for pos2 in range(n, -1, -1):

                if pos1 == m and pos2 == n:
                    continue

                first_match = (
                    pos1 < m and
                    pos2 < n and
                    (s[pos1] == p[pos2] or p[pos2] == '.')
                )

                if pos2 + 1 < n and p[pos2 + 1] == '*':
                    skip_star = dp[pos1][pos2 + 2]
                    use_star = first_match and dp[pos1 + 1][pos2]

                    dp[pos1][pos2] = skip_star or use_star
                elif pos2 < n:
                    dp[pos1][pos2] = (
                        first_match and
                        dp[pos1 + 1][pos2 + 1]
                    )

        return dp[0][0]

    def isMatchTabulizationOptimization(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [False] * (n + 1)
        dp[n] = True

        for pos1 in range(m, -1, -1):

            dpCopy = dp.copy()

            # Base case for current row
            dpCopy[n] = (pos1 == m)

            for pos2 in range(n - 1, -1, -1):

                first_match = (
                    pos1 < m
                    and
                    (
                        s[pos1] == p[pos2]
                        or
                        p[pos2] == '.'
                    )
                )

                if pos2 + 1 < n and p[pos2 + 1] == '*':

                    skip_star = dpCopy[pos2 + 2]

                    use_star = (
                        first_match
                        and
                        dp[pos2]
                    )

                    dpCopy[pos2] = (
                        skip_star or use_star
                    )

                else:

                    dpCopy[pos2] = (
                        first_match
                        and
                        dp[pos2 + 1]
                    )

            dp = dpCopy

        return dp[0]

print(Solution().isMatch(s = "aa", p = "a"))
print(Solution().isMatchTabulization(s = "aa", p = "a"))
print(Solution().isMatchTabulizationOptimization(s = "aa", p = "a"))