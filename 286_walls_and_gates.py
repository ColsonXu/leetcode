from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        inf = 2147483647
        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        seen = set()

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r, c, 1))
                    seen.add((r, c))

        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()

                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                for dir in directions:
                    row = r + dir[0]
                    col = c + dir[1]
                    
                    if (row, col) not in seen and row in range(m) and col in range(n) and rooms[row][col] != -1:
                        if rooms[row][col] <= inf and rooms[row][col] > 0:
                            rooms[row][col] = dist
                            q.append((row, col, dist+1))
                        seen.add((row,col))
