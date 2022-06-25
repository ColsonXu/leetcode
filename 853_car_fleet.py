class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(pos, s) for pos, s in zip(position, speed)])
        stack = []

        for pos, s in cars[::-1]:
            stack.append((target - pos) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
