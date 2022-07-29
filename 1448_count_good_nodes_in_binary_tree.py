class Solution:
    def goodNodes(self, root):
        def dfs(s, max_val):
            if not s:
                return 0

            res = 1 if s.val >= max_val else 0
            max_val = max(max_val, s.val)
            res += dfs(s.left, max_val)
            res += dfs(s.right, max_val)
            
            return res

        return dfs(root, root.val)
