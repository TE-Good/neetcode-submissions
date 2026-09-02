class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def ways(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            
            res = ways(i-1) + ways(i-2)
            memo[i] = res
            return res

        return ways(n)
        