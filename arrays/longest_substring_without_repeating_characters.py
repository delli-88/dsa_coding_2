class Solution:
    def lengthOfLongestSubstring(self, s):

        strMap = {}
        left = 0
        maxLen = 0

        for right in range(len(s)):

            if s[right] in strMap and strMap[s[right]]>=left:
                left = strMap[s[right]]+1
            maxLen = max(maxLen, right - left + 1)
            strMap[s[right]] = right

        return maxLen

sol = Solution()
print(sol.lengthOfLongestSubstring(s = "abcaabcdeb"))