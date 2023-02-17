def boom(x, y, field):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    field[y][x] = '.'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if nx < 0 or nx >= c or ny < 0 or ny >= r or field[ny][nx] == '.':
            continue
        field[ny][nx] = '.'

r, c, n = map(int, input().split())
field = [list(input()) for _ in range(r)]

sec = 1
while True:
    bombs = []
    for i in range(r):
        for j in range(c):
            if field[i][j] == 'O':
                bombs.append((j, i))
    
    sec += 1
    if sec > n:
        break
    field = [['O'] * c for _ in range(r)]
    
    sec += 1
    if sec > n:
        break
    for bomb in bombs:
        boom(bomb[0], bomb[1], field)
        
for x in field:
    print(''.join(x))
