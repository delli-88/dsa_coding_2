from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charMap = defaultdict(int)
        left = 0
        result = 0
        
        for right in range(len(s)):
            charMap[s[right]] += 1

            max_freq = max(charMap.values())
            
            while (right - left + 1) - max_freq > k:
                charMap[s[left]] -= 1
                left += 1
                max_freq = max(charMap.values())
            
            result = max(result, right - left + 1)
        
        return result

sol = Solution()
print(sol.characterReplacement(s = "BAAA", k = 0))