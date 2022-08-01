class Solution:
    def lastStoneWeight(self, stones):
        # turning negative to get max heap behavior from min heap
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            remain = abs(s1 - s2)
        
            if remain != 0:
                heapq.heappush(heap, -remain)
        return -heap[0] if heap else 0
