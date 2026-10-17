class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for ana in strs:
            key = [0] * 26

            for char in ana:
                key[ord(char) - ord("a")] += 1

            hash_map[tuple(key)].append(ana)

        return list(hash_map.values())
