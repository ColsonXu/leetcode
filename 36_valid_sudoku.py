class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True

        for i in range(9):
            valid = valid and self.check_unique(board[i])\
                          and self.check_unique([board[j][i] for j in range(9)])\
                          and self.check_unique(self.get_box(board, i))

        return valid


    def check_unique(self, check: List[str]) -> bool:
        seen = set()
        for x in check:
            if x != "." and x in seen:
                return False
            else:
                seen.add(x)
        return True


    def get_box(self, board: List[List[str]], box: int) -> List[str]:
        res = []
        for i in range(3):
            res.extend(board[box // 3 * 3 + i][(box % 3) * 3:(box % 3) * 3 + 3])
        return res
