class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            previous_end = output[-1][1]

            if start <= previous_end:
                output[-1][1] = max(previous_end, end)
            else:
                output.append([start, end])

        return output
