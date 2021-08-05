from collections import deque

def bfs():
    global color
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        y, x = queue.popleft()
        field[y][x] = color
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or field[ny][nx] > 1:
                continue
            if field[ny][nx] == 1:
                field[ny][nx] = color
                queue.append((ny, nx))
                
    color += 1

n = int(input())
field = [list(map(int, list(input()))) for _ in range(n)]

queue = deque()
# 집이 있는 곳을 나타내는 1과 구분하기 위해 2부터 시작
color = 2

# 너비 우선 탐색을 통해 단지의 번호를 붙여줌
for i in range(n):
    for j in range(n):
        if field[i][j] == 1:
            queue.append((i, j))
            bfs()
            
answer = []            
print(color - 2)
for i in range(2, color):
    answer.append(sum(x.count(i) for x in field))

# 단지의 개수를 오름차순으로 정렬하여 출력    
for x in sorted(answer):
    print(x)
