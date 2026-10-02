class Solution:
    def rob(self, nums: List[int]) -> int:
        max_arr = {}

        for i in range(len(nums)):
            if i == 0:
                max_arr[0] = nums[0]
                continue
            if i == 1:
                max_arr[1] = max(nums[0], nums[1])
                continue

            max_arr[i] = max(max_arr[i - 2] + nums[i], max_arr[i - 1])

        return max_arr[len(nums) - 1]
