class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list)
        for anagram in strs:
            anagram_key = "".join(sorted(anagram))
            anas[anagram_key].append(anagram)

        return anas.values()

