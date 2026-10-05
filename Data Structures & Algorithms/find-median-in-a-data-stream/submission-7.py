class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush_max(self.small, heapq.heappushpop(self.large, num))
        else:
            heapq.heappush(self.large, heapq.heappushpop_max(self.small, num))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        return (self.small[0] + self.large[0]) / 2
