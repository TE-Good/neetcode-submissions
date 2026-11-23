class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                need = 0 - nums[i] - nums[j]
                if need in seen:
                    res.add((nums[i], need, nums[j]))

                seen.add(nums[j])

        return list(res)
