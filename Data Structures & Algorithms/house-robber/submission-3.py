class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for num in nums:
            temp = rob1
            rob1 = rob2
            rob2 = max(rob2, temp + num)
        return rob2
        