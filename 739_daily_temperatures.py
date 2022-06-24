class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = []

        for i, t in enumerate(temps):
            if not stack or t < stack[-1]:
                stack.append((t, i))
            else:
                while stack[-1][0] < t:
                    res.append(i - stack[-1][1])
                    stack.pop()

        return res
