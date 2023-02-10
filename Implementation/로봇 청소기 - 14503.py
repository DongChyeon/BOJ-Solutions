def rotate_direction(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        
    can_clean = False
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if room[nr][nc] == 0:
            can_clean = True
            break
    
    if not can_clean:
        nr, nc = r - dr[d], c - dc[d]
        if nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1:
            break
        if room[nr][nc] == 1:
            break
        
        r, c = nr, nc
    else:
        for _ in range(4):
            d = rotate_direction(d)
            nr, nc = r + dr[d], c + dc[d]
            if room[nr][nc] == 0:
                r, c = nr, nc
                break
        
print(sum(x.count(2) for x in room))
