class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bot = l, r

                # save top left
                top_left = matrix[top][l + i]

                # rotate values
                matrix[top][l + i] = matrix[bot - i][l]
                matrix[bot - i][l] = matrix[bot][r - i]
                matrix[bot][r - i] = matrix[top + i][r]
                matrix[top + i][r] = top_left

            # move to new inner layer
            r -= 1
            l += 1
