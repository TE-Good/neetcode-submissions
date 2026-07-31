class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = {}
        for anagram in strs:
            sorted_anagram = sorted(anagram)
            anagram_key = "".join(sorted_anagram)
            
            if anas.get(anagram_key):
                anas[anagram_key].append(anagram)
            else:
                anas[anagram_key] = [anagram]

        return anas.values()

