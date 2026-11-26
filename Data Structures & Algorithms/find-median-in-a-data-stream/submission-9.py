class MedianFinder:
    def __init__(self):
        self.small = []  # max
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            # get the min from large
            large = heapq.heappushpop(self.large, num)
            # put onto small
            heapq.heappush_max(self.small, large)
        else:
            # put it into the small and get the largest
            small = heapq.heappushpop_max(self.small, num)
            # put onto large
            heapq.heappush(self.large, small)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        return (self.small[0] + self.large[0]) / 2
