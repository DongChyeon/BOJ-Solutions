from collections import deque

n, l, r = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque([(i, j)])
    union = [(i, j)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(field[nx][ny] - field[x][y]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    
    return union               

result = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    move_flag = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                countries = bfs(i, j)
                
                if len(countries) > 1:
                    move_flag = True
                    people = sum(field[x][y] for x, y in countries) // len(countries)
                    
                    for x, y in countries:
                        field[x][y] = people
    
    if not move_flag:
        break

    result += 1
    
print(result)
