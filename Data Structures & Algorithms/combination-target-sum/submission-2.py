class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(start, curr, amount):
            if amount == target:
                output.append(curr.copy())
                return
            if amount > target:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i, curr, amount + nums[i])
                curr.pop()

        dfs(0, [], 0)
        return output
