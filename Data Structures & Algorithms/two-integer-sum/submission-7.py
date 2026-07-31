
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i, num in enumerate(nums):
            diff = target - num

            if store.get(diff) is not None:
                return [store.get(diff), i]

            store[num] = i


            


