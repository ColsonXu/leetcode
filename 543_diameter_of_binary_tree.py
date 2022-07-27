class Solution:
    def diameterOfBinaryTree(self, root):
        res = [0]

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right)

            return max(left, right) + 1

        dfs(root)
        return res[0]
