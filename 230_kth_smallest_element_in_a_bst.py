class Solution:
    def kthSmallest(self, root, k):
        flattened = []
        
        def flatten(node):
            if not node:
                return None

            flatten(node.left)
            flattened.append(node.val)
            flatten(node.right)

        flatten(root)
        return flattened[k - 1]
