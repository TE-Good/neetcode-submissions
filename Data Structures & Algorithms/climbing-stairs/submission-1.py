class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            print("pre: ", one, two)
            temp = one
            one = one + two
            two = temp
            print("post: ", one, two)

        return one
        