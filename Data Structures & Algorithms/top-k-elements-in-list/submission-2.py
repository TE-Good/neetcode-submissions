class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        x = sorted(hash_map.items(), key=lambda x: x[1])[::-1]
        print(x)
        y = [x[0] for x in x]
        print(y)
        z = y [0:k]
        print(z)
        return z