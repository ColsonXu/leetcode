class Solution:
    def maxPathSum(self, root):
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            res[0] = max(res[0], node.val + left_max + right_max)
            
            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]
