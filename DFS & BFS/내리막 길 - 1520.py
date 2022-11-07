def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    # 방문하지 않은 경우 경로의 수를 0으로 초기화
    # 방문할 수 있는 곳이 없으면 (y, x)에서 (m-1, n-1)까지 갈 수 있는 경로의 수는 0
    dp[y][x] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1 or field[ny][nx] >= field[y][x]:
            continue
        dp[y][x] += dfs(nx, ny)
    
    return dp[y][x]

m, n = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(m)]
# dp[i][j] = (i, j)에서 (m-1, n-1)까지 갈 수 있는 경로의 수
dp = [[-1] * n for _ in range(m)]
dfs(0, 0)

print(dp[0][0])
