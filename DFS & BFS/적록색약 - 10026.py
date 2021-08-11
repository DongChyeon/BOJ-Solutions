import copy
from collections import deque

# 인접한 color를 탐색
def bfs(color, picture):
    global count
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        y, x = queue.popleft()
        picture[y][x] = 'X'
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or picture[ny][nx] != color:
                continue
            if picture[ny][nx] == color:
                picture[ny][nx] = 'X'
                queue.append((ny, nx))
                
    count += 1
    
n = int(input())
# 적록색약이 아닌 사람이 봤을 때의 그림
picture1 = [list(input()) for _ in range(n)]
# 적록색약인 사람이 봤을 때의 그림
picture2 = copy.deepcopy(picture1)
for i in range(n):
    for j in range(n):
        if picture2[i][j] == 'G':
            picture2[i][j] = 'R'

answer = []
queue = deque()
count = 0

# bfs를 통해 각 구역의 개수를 구함
for i in range(n):
    for j in range(n):
        if picture1[i][j] != 'X':
            queue.append((i, j))
            bfs(picture1[i][j], picture1)
answer.append(count)

count = 0
for i in range(n):
    for j in range(n):
        if picture2[i][j] != 'X':
            queue.append((i, j))
            bfs(picture2[i][j], picture2)
answer.append(count)
        
for x in answer:
    print(x, end=' ')
