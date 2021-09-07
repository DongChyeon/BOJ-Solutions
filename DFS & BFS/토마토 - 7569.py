from collections import deque

def bfs():
    # 너비 탐색할 때 x, y, z의 이동 범위
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    
    while queue:
        x, y, z, day = queue.popleft()
        
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            # 인덱스를 벗어날 시 무시
            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue
            if field[nz][ny][nx] == 0:
                # 큐에 넣기 전에 익음 표시
                field[nz][ny][nx] = 1
                queue.append((nx, ny, nz, day + 1))
            
    is_all_riped = True
    
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if field[z][y][x] == 0:
                    is_all_riped = False

    if is_all_riped:
        print(day)
    # 전부 다 익지 않았을 경우 -1 출력
    else:
        print(-1)

m, n, h = map(int, input().split())
field = []
answer = 0
for _ in range(h):
    field.append([list(map(int, input().split())) for _ in range(n)])

queue = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if field[z][y][x] == 1:
               queue.append((x, y, z, 0))
    
bfs()
