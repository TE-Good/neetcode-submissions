class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(i, curr, amount):
            if amount == target:
                output.append(curr.copy())
                return
            if amount > target:
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j, curr, amount + nums[j])
                curr.pop()

        dfs(0, [], 0)
        return output

        