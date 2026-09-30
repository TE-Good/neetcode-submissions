class MedianFinder:
    def __init__(self):
        # small: max heap, large: min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            # small is due the extra: pass num through large, large's min goes to small
            heapq.heappush_max(self.small, heapq.heappushpop(self.large, num))
        else:
            # small already holds the extra: pass num through small, small's max goes to large
            heapq.heappush(self.large, heapq.heappushpop_max(self.small, num))


    def OLDaddNum(self, num: int) -> None:
        heapq.heappush(self.large, heapq.heappushpop_max(self.small, num))
        if len(self.large) > len(self.small):
            heapq.heappush_max(self.small, heapq.heappop(self.large))

    def _EXAMPLE_addNum(self, num: int) -> None:
        # push num into small and pop small's max in one step
        top = heapq.heappushpop_max(self.small, num)
        # small's max moves to large, so everything in small <= everything in large
        heapq.heappush(self.large, top)
        # small may hold one extra element, large never may
        if len(self.large) > len(self.small):
            # move large's min back to small to restore the sizes
            top = heapq.heappop(self.large)
            heapq.heappush_max(self.small, top)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        return (self.small[0] + self.large[0]) / 2
