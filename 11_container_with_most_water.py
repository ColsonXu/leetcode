class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_vol = min(height[l], height[r]) * (r - l)
        while r > l:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
            max_vol = max(max_vol, min(height[l], height[r]) * (r - l))
        return max_vol
