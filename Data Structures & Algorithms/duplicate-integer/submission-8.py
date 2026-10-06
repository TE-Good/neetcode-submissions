class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        char_set = set()
        for num in nums:
            if num in char_set:
                return True
            char_set.add(num)
        return False
        