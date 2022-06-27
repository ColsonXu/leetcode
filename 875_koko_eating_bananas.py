class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        
        while l <= r:
            mid = (l + r) // 2
            h_needed = 0
            for x in piles:
                h_needed += math.ceil(x / mid)

            if h_needed <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
