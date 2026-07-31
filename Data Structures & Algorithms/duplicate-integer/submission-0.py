class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        logged_nums = {}

        for num in nums:
            if logged_nums.get(num):
                return True
            logged_nums[num] = True

        return False