import longest_common_subsequence
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = self.reverse(s)
        return longest_common_subsequence.Solution().longestCommonSubsequenceTabulizationOptimization(s, rev)
    
    def reverse(self, s: str):

        arr = []
        for i in range(len(s)):
            arr.append(s[i])

        
        start, end = 0, len(s) - 1

        while start<end:
            arr[start], arr[end] = arr[end], arr[start]
            start +=1
            end -=1
        
        return "".join(arr)
    
print(Solution().longestPalindromeSubseq(s = "bbbab"))