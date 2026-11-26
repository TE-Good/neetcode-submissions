class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for anagram in strs:
            key = [0] * 26

            for char in anagram:
                key[ord(char) - ord("a")] += 1

            hash_map[tuple(key)].append(anagram)

        return list(hash_map.values())
