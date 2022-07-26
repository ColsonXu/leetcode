class Solution:
    def invertTree(self, root):
        if root:
            tmp = root.right
            root.right = root.left
            root.left = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
            
        return root
