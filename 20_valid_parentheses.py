class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []
        
        for c in s:
            if c in pairs and stack and pairs[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0
