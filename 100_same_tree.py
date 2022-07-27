class Solution:
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
