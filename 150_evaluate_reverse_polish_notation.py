class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']
        stack = []
        
        for c in tokens:
            if c in op:
                e2 = int(stack.pop())
                e1 = int(stack.pop())
                if c == '+':
                    stack.append(e1 + e2)
                elif c == '-':
                    stack.append(e1 - e2)
                elif c == '*':
                    stack.append(e1 * e2)
                elif c == '/':
                    stack.append(e1 / e2)
            else:
               stack.append(c)

        return int(stack[-1])
