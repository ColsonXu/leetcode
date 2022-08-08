class Solution:
    def exist(self, board, word):
        path = set()

        def dfs(i, row, col):
            if i == len(word):
                return True
            if row < 0 or \
                    row >= len(board) or \
                    col < 0 or \
                    col >= len(board[0]) or \
                    board[row][col] != word[i] or \
                    (row, col) in path:
                return False

            path.add((row, col))
            
            res = dfs(i + 1, row + 1, col) or \
                    dfs(i + 1, row - 1, col) or \
                    dfs(i + 1, row, col + 1) or \
                    dfs(i + 1, row, col - 1)

            path.remove((row, col))

            return res
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(0, row, col):
                    return True

        return False
