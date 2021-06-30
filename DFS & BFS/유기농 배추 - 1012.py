import sys
from collections import deque
		
# 인접한 배추밭을 탐색
def BFS():
    global count
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        y, x = queue.popleft()
        field[y][x] = -1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n or field[ny][nx] == -1:
                continue
            if field[ny][nx] == 1:
                field[ny][nx] = -1
                queue.append((ny, nx))
                
    count += 1
		
input = sys.stdin.readline		
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    # 필드 초기화
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
        
    queue = deque([])
    count = 0

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                queue.append((i, j))
                BFS()
    
    print(count)
