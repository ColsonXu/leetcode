class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        comp = self.isSameTree(root, subRoot) or self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot)
        if comp:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, p, q):
        if p and q:
            if p.val != q.val:
                return False

            return self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right)
        elif p or q:
            return False
        else:
            return True
