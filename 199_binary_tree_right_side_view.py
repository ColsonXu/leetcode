class Solution:
    def rightSideView(self, root):
        levels = collections.defaultdict(list)
        queue = [(root, 0)]

        while queue:
            s = queue.pop()
            if s[0]:
                levels[s[1]].append(s[0].val)
                queue.append((s[0].right, s[1]+1))
                queue.append((s[0].left, s[1]+1))
        
        res = []
        for level in list(levels.values()):
            res.append(level[-1])
        
        return res
