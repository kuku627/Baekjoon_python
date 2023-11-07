def count_repaints(board):
    repaints = []

    for i in range(len(board) - 7):
        for j in range(len(board[i]) - 7):
            repaint_white = 0
            repaint_black = 0

            for x in range(8):
                for y in range(8):
                    if (x + y) % 2 == 0:
                        if board[i + x][j + y] != 'W':
                            repaint_white += 1
                    else:
                        if board[i + x][j + y] != 'B':
                            repaint_white += 1

            repaint_black = 64 - repaint_white
            repaints.append(min(repaint_white, repaint_black))

    return min(repaints)

N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_repaints = count_repaints(board)
print(min_repaints)
