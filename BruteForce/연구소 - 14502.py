from itertools import combinations
from collections import deque
import copy

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        y, x = queue.popleft()
        field[y][x] = 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n or field[ny][nx] == 1 or field[ny][nx] == 2:
                continue
            if field[ny][nx] == 0:
                field[ny][nx] = 2
                queue.append((ny, nx))

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for x in range(n)]

pool = []
# 벽을 세울 수 있는 곳을 pool에 담음
for y in range(len(lab)):
    for x in range(len(lab[y])):
        if lab[y][x] != 1 and lab[y][x] != 2:
            pool.append((y, x))
            
answer = 0

# 벽을 3개 세울 수 있는 경우의 수를 모두 구함
comb = list(combinations(pool, 3))
for x in comb:
    # 벽을 3개 세운 뒤
    field = copy.deepcopy(lab)
    for i in range(len(x)):
        field[x[i][0]][x[i][1]] = 1
        
    queue = deque([])
    count = 0
    
    # bfs를 통해 바이러스를 퍼지게 함
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 2:
                queue.append((y, x))
                bfs()
                
    # 안전 영역의 크기를 구해서 안전 영역 크기의 최댓값을 갱신함
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 0:
                count += 1

    answer = max(answer, count)
    
print(answer)
