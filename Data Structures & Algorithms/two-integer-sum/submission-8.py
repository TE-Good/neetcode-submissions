class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if hash_map.get(diff) is not None:
                return [hash_map.get(diff), i]
            hash_map[num] = i
        
        return []