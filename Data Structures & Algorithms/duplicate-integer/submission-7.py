class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = {}

        for num in nums:
            if record.get(num):
                return True
            record[num] = True
        return False