import sys
from collections import deque
input = sys.stdin.readline

# 주변 토마토를 계속 익게함
def BFS():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        y,x,day = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n or field[ny][nx] == -1:
                continue
            if field[ny][nx] == 0:
                field[ny][nx] = 1
                queue.append((ny, nx, day + 1))
                
    flag = False
        
    for i in range(n):
        for j in range(m):
            if field[i][j] == 0:
                flag = True
                break
                    
    if flag:
        print(-1)
    else:
        print(day)

m, n = map(int, input().split())
field = []
queue = deque([])

for _ in range(n):
    field.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            queue.append((i,j,0))
    
BFS()
