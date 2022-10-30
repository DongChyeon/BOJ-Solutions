from collections import deque
import copy

# 너비 우선 탐색을 통해 다른 육지까지의 최단 거리를 구함
def bfs(island):
    global answer
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            
            if island[ny][nx] == 'L':
                island[ny][nx] = 'X'
                distance[ny][nx] = distance[y][x] + 1
                queue.append((ny, nx))

r, c = map(int, input().split())
island = [list(input()) for _ in range(r)]
answer = 0

for i in range(r):
    for j in range(c):
        # 각 육지를 시작점으로 설정해 다른 육지로의 최단거리를 구함
        # 그 중 가장 최단거리가 먼 것을 구함
        if island[i][j] == 'L':
            distance = [[0 for _ in range(c)] for _ in range(r)]
            
            island_copy = copy.deepcopy(island)
            island_copy[i][j] = 'X'
            queue = deque([(i, j)])
            bfs(island_copy)
            
            answer = max(answer, max(map(max, distance)))

print(answer)
