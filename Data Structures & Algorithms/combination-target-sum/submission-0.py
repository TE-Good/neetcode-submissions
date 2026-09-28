class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
            res = []
            def dfs(start, cur, total):
                if total == target:
                    res.append(cur.copy()); return
                if total > target:
                    return
                for j in range(start, len(nums)):
                    cur.append(nums[j])
                    dfs(j, cur, total + nums[j])   # j, not j+1 — that IS "reuse allowed"
                    cur.pop()
            dfs(0, [], 0)
            return res