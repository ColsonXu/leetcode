class Solution:
    def partition(self, s):
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return

            for j in range(i, len(s)):
                if s[i:j] == s[j:i:-1]:
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
