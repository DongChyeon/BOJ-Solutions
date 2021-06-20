from collections import deque

# 바깥쪽 공기 탐색
# 0 : 안쪽 공기, 1 : 치즈, 2 : 바깥쪽 공기
def BFS(y, x):
    queue = deque([(y, x)])
    
    while queue:
        y, x = queue.popleft()
        cheese[y][x] = 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n or cheese[ny][nx] == 1 or cheese[ny][nx] == 2:
                continue
            if cheese[ny][nx] == 0:
                cheese[ny][nx] = 2
                queue.append((ny, nx))

n, m = map(int, input().split())
cheese = []
for _ in range(n):
    cheese.append(list(map(int, input().split())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
day = 0

# 바깥공기 탐색
BFS(0, 0)

while sum(map(sum, cheese)) != (2 * n * m):
    targets = []

    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                flag = False
                
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or cheese[ny][nx] == 1 or cheese[ny][nx] == 0:
                        continue
                    if cheese[ny][nx] == 2:
                        flag = True
                        break
                
                if flag:
                    targets.append((i, j))
    
    # 남은 치즈의 개수                
    remain = 0
    for x in cheese:
        remain += x.count(1)
    
    # 바깥 공기와 두 변 이상 맞닿아 있는 치즈를 녹임                
    for target in targets:
        cheese[target[0]][target[1]] = 0
        # 바깥 공기 갱신
        BFS(target[0], target[1])
    
    day += 1

print(day)
print(remain)
