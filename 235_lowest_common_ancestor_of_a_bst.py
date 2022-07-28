class Solution:

    # Not taking advantage of the fact that this is a BST
    def lowestCommonAncestor(self, root, p, q):
        def bfs(s, target):
            seen = set()
            queue = []
            queue.append(s)
            seen.add(s)
            
            while queue:
                s = queue.pop()
                if s == target:
                    return True
                if s:
                    queue.append(s.left)
                    queue.append(s.right)

        if p == q:
            return p

        p_in_left = bfs(root.left, p)
        q_in_left = bfs(root.left, q)

        p_in_right = bfs(root.right, p)
        q_in_right = bfs(root.right, q)

        if (p_in_left and q_in_right) or \
                (p_in_right and q_in_left) or \
                root == p or root == q:
            return root
        elif p_in_left and q_in_left:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

    # Improved version taking advantage of BST invariant
    def lca(self, root, p, q):
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
