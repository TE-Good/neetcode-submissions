class MedianFinder:
    def __init__(self):
        # max heap
        self.small = []
        # min heap
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            # put onto large and the min
            min_num = heapq.heappushpop(self.large, num)
            # put min on small
            heapq.heappush_max(self.small, min_num)
        else:
            # put onto min, get the max
            max_num = heapq.heappushpop_max(self.small, num)
            # put onto large
            heapq.heappush(self.large, max_num)


    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.small[0] + self.large[0]) / 2
        return self.small[0]
