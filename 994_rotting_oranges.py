from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        time = 0
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while fresh > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
            
                if row - 1 >= 0 and grid[row-1][col] == 1:
                    grid[row-1][col] = 2
                    q.append((row-1, col))
                    fresh -= 1
                if row + 1 < m and grid[row+1][col] == 1:
                    grid[row+1][col] = 2
                    q.append((row+1, col))
                    fresh -= 1
                if col - 1 >= 0 and grid[row][col-1] == 1:
                    grid[row][col-1] = 2
                    q.append((row, col-1))
                    fresh -= 1
                if col + 1 < n and grid[row][col+1] == 1:
                    grid[row][col+1] = 2
                    q.append((row, col+1))
                    fresh -= 1
            time += 1

        return -1 if fresh > 0 else time
