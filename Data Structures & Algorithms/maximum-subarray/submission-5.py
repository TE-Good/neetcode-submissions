class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        total_max = nums[0]
        
        for num in nums:
            if curr_max < 0:
                curr_max = 0

            curr_max += num
            total_max = max(total_max, curr_max)
        return total_max

        