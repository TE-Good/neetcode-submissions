class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(i, curr, amount):
            if amount == target:
                return output.append(curr.copy())
            if amount > target:
                return 

            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j, curr, amount + nums[j])
                curr.pop()

        dfs(0, [], 0)
        return output
        