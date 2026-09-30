class MedianFinder:
    def __init__(self):
        # small: max heap, large: min heap
        # small will only be equal or +1 in length at any time
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # If they're equal length, push num into large and get the min to add to small.
        if len(self.small) == len(self.large):
            # small is due the extra: pass num through large, large's min goes to small
            heapq.heappush_max(self.small, heapq.heappushpop(self.large, num))
        # Vice versa.
        else:
            # small already holds the extra: pass num through small, small's max goes to large
            heapq.heappush(self.large, heapq.heappushpop_max(self.small, num))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        return (self.small[0] + self.large[0]) / 2
