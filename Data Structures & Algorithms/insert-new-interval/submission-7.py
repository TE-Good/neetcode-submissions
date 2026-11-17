class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        l, r = 0, len(intervals)

        while l < r and intervals[l][1] < newInterval[0]:
            res.append(intervals[l])
            l += 1

        while l < r and intervals[l][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[l][0]),
                max(newInterval[1], intervals[l][1]),
            ]
            l += 1

        return res + [newInterval] + intervals[l:]
