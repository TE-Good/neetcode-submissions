class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            min_from_large = heapq.heappushpop(self.large, num)
            heapq.heappush_max(self.small, min_from_large)
        else:
            max_from_small = heapq.heappushpop_max(self.small, num)
            heapq.heappush(self.large, max_from_small)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        
        return (self.small[0] + self.large[0]) /2
        
        