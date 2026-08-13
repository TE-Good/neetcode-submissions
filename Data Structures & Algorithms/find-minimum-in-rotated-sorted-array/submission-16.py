class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        pivot = nums[l]

        while l <= r:
            if nums[l] <= nums[r]:
                return min(pivot, nums[l])

            m = (l + r) // 2
            pivot = min(pivot, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return pivot
