from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagrams_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagrams_map:
                anagrams_map[sorted_word] = []
            anagrams_map[sorted_word].append(word)
        
        return list(anagrams_map.values())
    
    def groupAnagramsOpti(self, strs):
        anagrams_map = defaultdict(list)
        for word in strs:
            charArr = [0] * 26
            for ch in word:
                charArr[ord(ch)-97]+=1
            anagrams_map[tuple(charArr)].append(word)
        print(anagrams_map)
        
        return list(anagrams_map.values())
        

sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagramsOpti(strs = ["eat","tea","tan","ate","nat","bat"]))