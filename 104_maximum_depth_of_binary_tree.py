class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)