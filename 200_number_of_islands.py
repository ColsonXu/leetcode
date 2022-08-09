class Solution:
    def numIslands(self, grid):
        res = [0]
        seen = set()
        
        def bfs(row, col):
            if grid[row][col] == "1" and (row, col) not in seen:
                res[0] += 1
            
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                seen.add((r, c))
                if grid[r][c] == "0":
                    continue
                if r > 0 and (r-1, c) not in seen:
                    stack.append((r-1, c))
                if r < len(grid) - 1 and (r+1, c) not in seen:
                    stack.append((r+1, c))
                if c > 0 and (r, c-1) not in seen:
                    stack.append((r, c-1))
                if c < len(grid[0]) - 1 and (r, c+1) not in seen:
                    stack.append((r, c+1))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                bfs(row, col)

        return res[0]
