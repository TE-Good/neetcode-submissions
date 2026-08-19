class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while nums[l] > nums[r]:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m

        return nums[l]

        # l, r = 0, len(nums) - 1

        # while l < r:
        #     if nums[l] <= nums[r]:      # window already sorted
        #         return nums[l]

        #     m = (l + r) // 2

        #     if nums[l] <= nums[m]:      # left half sorted -> min is right of m
        #         l = m + 1
        #     else:                       # pivot in [l..m] -> m still a candidate
        #         r = m

        # return nums[l]
