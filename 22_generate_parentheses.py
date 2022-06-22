class Solution:
    def generateParenthesis(self, n):
        stack = []
        res = []

        def helper(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))

            if opened < n:
                stack.append("(")
                helper(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                helper(opened, closed + 1)
                stack.pop()

        helper(0, 0)
        return res
