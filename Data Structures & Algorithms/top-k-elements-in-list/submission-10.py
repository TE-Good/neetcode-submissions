class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        freqs = [[] for i in range(len(nums) + 1)]
        for num, count in counts.items():
            freqs[count].append(num)

        output = []
        for freq in freqs[::-1]:
            for num in freq:
                output.append(num)
                if len(output) == k:
                    return output
