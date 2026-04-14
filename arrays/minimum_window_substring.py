class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        charMap = {}
        for ch in t:
            charMap[ch] = charMap.get(ch, 0) + 1

        requiredCount = len(t)

        left = 0
        count = 0
        minLength = float("inf")
        minLenIdx = -1

        for right in range(len(s)):

            if charMap.get(s[right], 0) > 0:
                count += 1

            charMap[s[right]] = charMap.get(s[right], 0) - 1

            while count == requiredCount:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    minLenIdx = left

                charMap[s[left]] = charMap.get(s[left], 0) + 1

                if charMap[s[left]] > 0:
                    count -= 1

                left += 1

        if minLenIdx == -1:
            return ""

        return s[minLenIdx:minLenIdx + minLength]

sol = Solution()
print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC"))