from collections import deque
import sys

def bfs():
    global count, areas
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    size = 0
    while queue:
        y, x = queue.popleft()
        size += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or field[ny][nx] == 1:
                continue
            if field[ny][nx] == 0:
                field[ny][nx] = 1
                queue.append((ny, nx))
                
    count += 1
    areas.append(size)

input = sys.stdin.readline
m, n, k = map(int, input().split())
field = [[0 for _ in range(n)] for _ in range(m)]
count, areas, queue = 0, [], deque()

# 직사각형이 있는 영역을 1로 칠함
for _ in range(k):
    a, b, c, d = map(int, input().split())
    x1, y1 = a, m - d
    x2, y2 = c - 1, m - b - 1 
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            field[y][x] = 1

# 칠하지 않은 영역에 대해 BFS 탐색         
for y in range(m):
    for x in range(n):
        if field[y][x] == 0:
            queue.append((y, x))
            field[y][x] = 1
            bfs()
            
print(count)
for x in sorted(areas):
    print(x, end=' ')
