class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        coords = {}
        for i in range(1, 10):
            coords[i] = [set(), set(), set()]
        # print(type(coords[1][0]))
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    quadrant = int((i // 3) * 3 + (j // 3))
                    if (
                    i in coords[num][0] 
                    or j in coords[num][1]
                    or quadrant in coords[num][2]
                    ):
                        return False
                    else:
                        coords[num][0].add(i)
                        coords[num][1].add(j)
                        coords[num][2].add(quadrant)
        print(coords)
        return True