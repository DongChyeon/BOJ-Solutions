board = [list(map(int, input().split())) for _ in range(19)]

def checkWin(x, y, player):
    cnt = 1
    # ↖ 방향 체크
    nx, ny = x, y
    while True:
        nx, ny = nx - 1, ny - 1
        if nx < 0 or ny < 0 or board[ny][nx] != player:
            break
        cnt += 1
    ans_x, ans_y = nx + 1, ny + 1
    # ↘ 방향 체크
    nx, ny = x, y
    while True:
        nx, ny = nx + 1, ny + 1
        if nx > 18 or ny > 18 or board[ny][nx] != player:
            break
        cnt += 1
    if cnt == 5:
        return (ans_x, ans_y)
    
    cnt = 1
    # ↙ 방향 체크 
    nx, ny = x, y
    while True:
        nx, ny = nx - 1, ny + 1
        if nx < 0 or ny > 18 or board[ny][nx] != player:
            break
        cnt += 1
    ans_x, ans_y = nx + 1, ny - 1
    # ↗ 방향 체크
    nx, ny = x, y
    while True:
        nx, ny = nx + 1, ny - 1
        if nx > 18 or ny < 0 or board[ny][nx] != player:
            break
        cnt += 1
    if cnt == 5:
        return (ans_x, ans_y)

    cnt = 1
    # ← 방향 체크
    nx, ny = x, y
    while True:
        nx -= 1
        if nx < 0 or board[ny][nx] != player:
            break
        cnt += 1
    ans_x, ans_y = nx + 1, ny
    # → 방향 체크
    nx, ny = x, y
    while True:
        nx += 1
        if nx > 18 or board[ny][nx] != player:
            break
        cnt += 1
    if cnt == 5:
        return (ans_x, ans_y)

    cnt = 1
    # ↑ 방향 체크
    nx, ny = x, y
    while True:
        ny -= 1
        if ny < 0 or board[ny][nx] != player:
            break
        cnt += 1
    ans_x, ans_y = nx, ny + 1
    # ↓ 방향 체크
    nx, ny = x, y
    while True: 
        ny += 1
        if ny > 18 or board[ny][nx] != player:
            break
        cnt += 1
    if cnt == 5:
        return (ans_x, ans_y)
            
    return (-1, -1)

for y in range(19):
    for x in range(19):
        if board[y][x] == 1:
            ans_x, ans_y = checkWin(x, y, 1)
            if ans_x != -1 and ans_y != -1:
                print(1)
                print(ans_y + 1, ans_x + 1)
                exit(0)
        elif board[y][x] == 2:
            ans_x, ans_y = checkWin(x, y, 2)
            if ans_x != -1 and ans_y != -1:
                print(2)
                print(ans_y + 1, ans_x + 1)
                exit(0)
            
print(0)
