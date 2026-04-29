class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = 0
        startIdx = 0

        for i in range(len(s)):
            start = i
            end = i

            # handle duplicates
            while end + 1 < len(s) and s[end] == s[end + 1]:
                end += 1

            # expand
            while start >= 0 and end < len(s) and s[start] == s[end]:
                currLen = end - start + 1
                if currLen > longest:
                    longest = currLen
                    startIdx = start
                start -= 1
                end += 1

        return s[startIdx:startIdx + longest]
    
print(Solution().longestPalindrome(s = "babbad"))