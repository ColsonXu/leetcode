class Solution:
    def maxAreaOfIsland(self, grid):
        seen = set()
        
        def dfs(r, c):
            if ((r, c) in seen
                    or r not in range(len(grid))
                    or c not in range(len(grid[0]))
                    or grid[r][c] == 0):
                return 0
            seen.add((r, c))
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                area = max(area, dfs(row, col))

        return area
