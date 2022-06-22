class MinStack:

    slots = ("stack", "min")

    def __init__(self):
        self.stack = []
        self.min = [99999999999999]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min[-1]:
            self.min.append(val)


    def pop(self) -> None:
        val = self.stack.pop()
        if self.min[-1] == val:
            self.min.pop()
        return val


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return int(self.min[-1])
