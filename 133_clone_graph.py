from collections import deque

class Solution:
    def cloneGraph(self, node):
        res = Node(node.val, [])
        seen = set()

        def dfs(prev, queue):
            curr = queue.popleft()
            for n in curr.neighbors:
                prev.neighbors.append(Node(n.val, []))
                if n not in seen:
                    dfs(n, [])
