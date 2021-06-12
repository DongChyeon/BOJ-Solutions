from collections import deque

n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]

distance = [[0] * m for _ in range(n)]
distance[0][0] = 1

queue = deque([(0, 0)])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= m or ny < 0 or ny >= n or maze[ny][nx] == '0':
            continue
        
        if maze[ny][nx] == '1':
            # 돌아갈 수 없도록 벽으로 처리
            maze[ny][nx] = '0'
            queue.append((nx, ny))
            distance[ny][nx] = distance[y][x] + 1
            
print(distance[n - 1][m - 1])
