from collections import deque
import sys

def bfs():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    queue = deque([(0, 0, 0)])
    
    while queue:
        x, y, z = queue.popleft()
        
        if x == m - 1 and y == n - 1:
            return visited[y][x][z]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                # 벽을 부수고 이동하는 경우
                if field[ny][nx] == 1 and z == 0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    queue.append((nx, ny, 1))
                # 벽을 부수지 않고 이동하는 경우    
                elif field[ny][nx] == 0 and visited[ny][nx][z] == 0:
                    visited[ny][nx][z] = visited[y][x][z] + 1
                    queue.append((nx, ny, z))
                    
    return -1

input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(map(int, input().rstrip('\n'))) for _ in range(n)]

print(bfs())
