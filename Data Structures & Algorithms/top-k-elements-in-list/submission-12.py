class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        freqs = [[] for i in range(len(nums)+1)]
        for num, count in counts.items():
            freqs[count].append(num)

        res = []
        for freq in freqs[::-1]:
            for num in freq:
                res.append(num)
                if len(res) == k:
                    return res