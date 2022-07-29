class Solution:
    # bruteforce
    def isValidBST(self, root):
        if not root:
            return True

        def larger_in_left(node, target):
            if not node:
                return False

            if node.val >= target:
                return True

            return larger_in_left(node.left, target) or\
                    larger_in_left(node.right, target)

        def less_in_right(node, target):
            if not node:
                return False

            if node.val <= target:
                print(node.val, target)
                return True

            return less_in_right(node.left, target) or \
                    less_in_right(node.right, target)

        if larger_in_left(root.left, root.val) or less_in_right(root.right, root.val):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

    # better way
    def validBST(self, root):
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val and node.val < right):
                return False

            return valid(node.left, left, node.val) and \
                    valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))
