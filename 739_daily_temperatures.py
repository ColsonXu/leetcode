class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((t, i))

        return res
