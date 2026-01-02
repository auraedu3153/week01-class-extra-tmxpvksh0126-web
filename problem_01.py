def snail_board(col: int, row: int, clockwise=True) -> list[list[int]]:
    """
    행 개수 (row)와 열 개수 (col)을 받아 달팽이 배열을 만드는 함수.
    시작 위치는 (0, 0)이고, 방향은 인자 clockwise에 따라 시계방향 또는 반시계방향으로 설정됨.
    """
    board = [[0]*(row+2) for _ in range(col+2)]
    board[0] = [1]*(row+2)
    board[-1] = [1]*(row+2)
    for i in range(col+2):
        board[i][0]=1
        board[i][-1]=1
    direction = 0
    #0:Right / 1: Down / 2: Left / 3: Up

    n = 1
    x = 1
    y = 1
    for _ in range(row*col):
        d = direction %4
        if clockwise:
            board[y][x] = n
            if d == 0:
                if board[y][x+1] != 0:
                    y += 1
                    direction += 1
                else:
                    x += 1
            elif d == 1:
                if board[y+1][x] != 0:
                    x -= 1
                    direction += 1
                else:
                    y += 1
            elif d == 2:
                if board[y][x-1]:
                    y -= 1
                    direction += 1
                else:
                    x -= 1
            elif d == 3:
                if board[y-1][x] != 0:
                    x += 1
                    direction += 1
                else:
                    y -= 1
        else:
            board[x][y] = n
            if d == 0:
                if board[x+1][y] != 0:
                    y += 1
                    direction += 1
                else:
                    x += 1
            elif d == 1:
                if board[x][y+1] != 0:
                    x -= 1
                    direction += 1
                else:
                    y += 1
            elif d == 2:
                if board[x-1][y]:
                    y -= 1
                    direction += 1
                else:
                    x -= 1
            elif d == 3:
                if board[x][y-1] != 0:
                    x += 1
                    direction += 1
                else:
                    y -= 1
        n += 1
        
    return [rows[1:-1] for rows in board[1:-1]]

print(snail_board(4,6,False))