from collections import deque

def bfs(has_gram, go_to_gram):
    global answer, queue, visited
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while queue:
        count, x, y = queue.popleft()
        
        if go_to_gram:
            if field[y][x] == 2:
                queue = deque([(count, x, y)])
                # 그람을 가지면 뚫을 수 없던 벽도 뚫을 수 있기 때문에 방문 정보 초기화
                visited = [[False] * m for _ in range(n)]
                visited[y][x] = True
                return bfs(True, False)
        else:
            if x == m - 1 and y == n - 1:
                return count
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
                continue
            if not has_gram and field[ny][nx] == 1:
                continue
            queue.append((count + 1, nx, ny))
            visited[ny][nx] = True
            
    return t + 1    # 도달하지 않을 경우 t + 1을 반환해 Fail이 나오도록 함
        
n, m, t = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
visited[0][0] = True
queue = deque([(0, 0, 0)])
route1 = bfs(False, False)  # 그람을 거치지 않고 가는 루트

visited = [[False] * m for _ in range(n)]
visited[0][0] = True
queue = deque([(0, 0, 0)])
route2 = bfs(False, True)   # 그람을 거치고 가는 루트

answer = min(route1, route2)

if answer <= t:
    print(answer)
else:
    print('Fail')
