class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        boxes = [[False] * 10 for _ in range(9)]

        # (0,0) in top left
        colSeen = [[False] * 10 for _ in range(9)]
        for y in range(n):
            rowSeen = [False] * 10
            for x in range(n):
                boxX = x // 3
                boxY = y // 3

                box = boxes[boxX + boxY * 3]
                digit = board[y][x]
                if digit == ".":
                    continue
                digit = int(digit)

                if box[digit]:
                    return False
                else:
                    box[digit] = True

                if rowSeen[digit]:
                    return False
                else:
                    rowSeen[digit] = True

                if colSeen[x][digit]:
                    return False
                else:
                    colSeen[x][digit] = True

        return True                


        