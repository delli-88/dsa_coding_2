from collections import defaultdict
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1Map = defaultdict(int)
        s2WindowMap = defaultdict(int)

        for i in range(len(s1)):
            s1Map[s1[i]] +=1
        
        for j1 in range(len(s1)):
            s2WindowMap[s2[j1]]+=1
        
        if s1Map == s2WindowMap:
            return True
        
        for j2 in range(len(s1), len(s2)):
            s2WindowMap[s2[j2-len(s1)]] -= 1
            if s2WindowMap[s2[j2-len(s1)]] <=0:
                del s2WindowMap[s2[j2-len(s1)]]
            s2WindowMap[s2[j2]]+=1
            if s1Map == s2WindowMap:
                return True
        return False

    def checkInclusionOpti(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1Arr = [0] * 26
        s2Arr = [0] * 26

        for i in range(len(s1)):
            s1Arr[ord(s1[i]) - ord("a")] +=1
        
        for j1 in range(len(s1)):
            s2Arr[ord(s2[j1]) - ord("a")]+=1
        
        if s1Arr == s2Arr:
            return True
        
        for j2 in range(len(s1), len(s2)):
            s2Arr[ord(s2[j2-len(s1)]) - ord("a")]-=1
            s2Arr[ord(s2[j2]) - ord("a")]+=1
            if s1Arr == s2Arr:
                return True
        return False
    
    def checkInclusionMatches(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        window = [0] * 26
        
        # Build frequency arrays
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        # Count initial matches
        matches = 0
        for i in range(26):
            if s1_count[i] == window[i]:
                matches += 1
        
        left = 0
        
        # Slide the window
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Add new character (right)
            idx = ord(s2[right]) - ord('a')
            window[idx] += 1
            
            if window[idx] == s1_count[idx]:
                matches += 1
            elif window[idx] == s1_count[idx] + 1:
                matches -= 1
            
            # Remove left character
            idx = ord(s2[left]) - ord('a')
            window[idx] -= 1
            
            if window[idx] == s1_count[idx]:
                matches += 1
            elif window[idx] == s1_count[idx] - 1:
                matches -= 1
            
            left += 1
        
        return matches == 26
    
sol = Solution()
print(sol.checkInclusion(s1 = "ab", s2 = "eidboaooo"))
print(sol.checkInclusionOpti(s1 = "ab", s2 = "eidbaooo"))
print(sol.checkInclusionMatches(s1 = "ab", s2 = "eidbaooo"))