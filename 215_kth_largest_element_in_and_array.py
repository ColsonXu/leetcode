import heapq

class Solution:
    def findKthLargest(self, nums, k):
        nums = [-x for x in nums]
        heapq.heapify(nums)

        while k > 0:
            heapq.heappop(nums)
            k -= 1

        return -heapq.heappop(nums)

