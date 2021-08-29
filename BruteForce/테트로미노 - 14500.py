# ㅗ자 모양 말고는 길이가 4인 dfs를 통해 해결 가능
def dfs(x, y, total, length):
    global answer
    
    # 길이가 4일 경우 종료시키고 정답 갱신
    if length >= 4:
        answer = max(answer, total)
        return
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # 범위를 벗어난 경우 무시
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        
        if not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, total + field[ny][nx], length + 1)
            # 회전, 대칭을 위해 재방문 가능하도록 초기화
            visited[ny][nx] = False
            
n, m = map(int, input().split())
field = [list(map(int, input().split())) for x in range(n)]
visited = [[False] * m for x in range(n)]
# ㅗ자 모양 조각 이동 범위 (y이동값, x이동값)
part = [[(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 1), (1, 0), (1, 1), (1, 2)], [(0, 0), (1, 0), (2, 0), (1, 1)], [(1, 0), (0, 1), (1, 1), (2, 1)]]

answer = 0

for y in range(n):
    for x in range(m):
        visited[y][x] = True
        dfs(x, y, field[y][x], 1)
        # 회전, 대칭을 위해 재방문 가능하도록 초기화
        visited[y][x] = False
        
        # ㅗ자 모양 검사
        for i in part:
            isOut = False
            total = 0
            
            for j in i:
                nx, ny = x + int(j[1]), y + int(j[0])
            
                # 바깥으로 삐져나간 경우 검사 종료
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    isOut = True
                    break
                
                total += field[ny][nx]
        
            if not isOut:        
                answer = max(answer, total)
        
print(answer)
