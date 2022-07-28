class Solution:
    def levelOrder(self, root):
        res = collections.defaultdict(list)
        queue = [(root, 0)]

        while queue:
            s = queue.pop()
            if s[0]:
                res[s[1]].append(s[0].val)
                queue.append((s[0].right, s[1]+1))
                queue.append((s[0].left, s[1]+1))
        
        return list(res.values())
            
