class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index_2, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                index_1 = hash_map.get(diff)
                return [index_1, index_2]
            hash_map[num] = index_2

        return []