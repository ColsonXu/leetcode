class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        
        for i, h in enumerate(heights):
            last = i
            while stack and h < stack[-1][1]:
                prev_i, prev_h = stack.pop()
                res = max(res, prev_h * (i - prev_i))
                last = prev_i
            stack.append((last, h))
        
        for i, h, in stack:
            res = max(res, h * (len(heights) - i))
        
        return res
