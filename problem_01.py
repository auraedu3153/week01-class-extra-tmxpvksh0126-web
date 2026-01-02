def snail_board(row: int, col: int, clockwise=True) -> list[list[int]]:
    """
    행 개수 (row)와 열 개수 (col)을 받아 달팽이 배열을 만드는 함수.
    시작 위치는 (0, 0)이고, 방향은 인자 clockwise에 따라 시계방향 또는 반시계방향으로 설정됨.
    """
    board = [[0]*(row+2) for _ in range(col+2)]

    direction = 0
    #0:Right / 1: Down / 2: Left / 3: Up

    n = 1
    x = 0
    y = 0
    for _ in range(row*col):
        board[x][y] = n
        n += 1
        d = direction %4
        if clockwise:
            if d == 0:
                if x == row-1 or board[x+1][y] != 0:
                    y += 1
                    direction += 1
                else:
                    x += 1
            elif d == 1:
                if y == col-1 or board:
                    x -= 1
                    direction += 1
                else:
                    y += 1
            elif d == 2:
                if x == 0:
                    y += 1
                    direction += 1
                else:
                    x -= 1

board = [[0]*5 for _ in range(4)]
print([rows[1:-1] for rows in board[1:-1]])