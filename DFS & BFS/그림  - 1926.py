import sys

sys.setrecursionlimit(10**7)

def dfs(y, x):
    global picture_size
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    picture[y][x] = 0
    picture_size += 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if m > nx >= 0 and n > ny >= 0:
            if picture[ny][nx] == 1:
                dfs(ny, nx)

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
picture_count = 0
answer = 0

for y in range(n):
    for x in range(m):
        if picture[y][x] == 1:
            picture_count += 1
            picture_size = 0
            dfs(y, x)
            answer = max(answer, picture_size)

print(picture_count)
print(answer)

-----------------------------------------------------------------------------

from collections import deque

def bfs(y, x):
    global answer
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque([(y, x)])
    picture[y][x] = 0
    
    size = 0
    while queue:
        y, x = queue.popleft()
        size += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if m > nx >= 0 and n > ny >= 0:
                if picture[ny][nx] == 1:
                    picture[ny][nx] = 0
                    queue.append((ny, nx))
                    
    answer = max(answer, size)

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
picture_count = 0
answer = 0

for y in range(n):
    for x in range(m):
        if picture[y][x] == 1:
            picture_count += 1
            bfs(y, x)

print(picture_count)
print(answer)
