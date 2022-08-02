import math
import heapq

class Solution:
    def kClosest(self, points, k):
        def dist(p):
            return math.sqrt(p[0] ** 2 + p[1] ** 2)

        for i, p in enumerate(points):
            points[i] = (dist(p), p[0], p[1])

        heapq.heapify(points)
        
        res = []

        for _ in range(k):
            res.append(heapq.heappop(points))

        return res
