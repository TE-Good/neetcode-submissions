class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        reverse_sort = sorted(hash_map.items(), key=lambda x: x[1])[::-1]
        return [x[0] for x in reverse_sort][0:k]