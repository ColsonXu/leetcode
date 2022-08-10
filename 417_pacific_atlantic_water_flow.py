class Solution:
    def pacificAtlantic(self, heights):
        ROW, COL = len(heights), len(heights[0])
        at, pac = set(), set()

        def dfs(r, c, seen, prev):
            if (
                    (r, c) in seen
                    or r not in range(ROW)
                    or c not in range(COL)
                    or heights[r][c] < prev
            ):
                return

            seen.add((r, c))
            dfs(r + 1, c, seen, heights[r][c])
            dfs(r - 1, c, seen, heights[r][c])
            dfs(r, c + 1, seen, heights[r][c])
            dfs(r, c - 1, seen, heights[r][c])
        
        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW - 1, c, at, heights[ROW - 1][c])

        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL - 1, at, heights[r][COL - 1])

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in at:
                    res.append([r, c])

        return res
