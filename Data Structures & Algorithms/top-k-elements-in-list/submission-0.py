class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        k_counts = sorted(counts.items(), key=lambda x: x[1])[-k:]
        
        return [num for num, _count in k_counts]
        