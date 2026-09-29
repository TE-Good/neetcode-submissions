class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        working_sum = 0

        for num in nums:
            if working_sum < 0:
                working_sum = 0
            
            working_sum += num
            max_sum = max(max_sum, working_sum)

        return max_sum
        