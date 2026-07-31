class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for st in strs:
            sorted_str = "".join(sorted(st))
            hash_map[sorted_str].append(st)

        return [v for v in hash_map.values()]

        