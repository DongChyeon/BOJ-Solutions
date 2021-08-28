from collections import deque
import copy

# 인접한 영역을 탐색
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
            
            # 범위를 벗어나거나 잠겨있거나 색칠한 영역은 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n or field[ny][nx] == -1 or field[ny][nx] > 100:
                continue
            if field[ny][nx] != -1:
                field[ny][nx] = color
                queue.append((ny, nx))
                
    color += 1

n = int(input())
area = [list(map(int, input().split())) for x in range(n)]
max_height = max(map(max, area)) + 1
answer = 0

queue = deque()

# height = 내리는 비의 양
for height in range(1, max_height + 1):
    field = copy.deepcopy(area)
    
    # 내리는 비의 양보다 낮은 지역을 잠기게 함 (-1 : 잠긴 지역)
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] < height:
                field[y][x] = -1
    
    # 높이와 구분하기 위해 101부터 시작
    color = 101
    
    # 너비 우선 탐색을 통해 잠기지 않는 구역의 개수를 구함
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] != -1 and field[y][x] < 101:
                queue.append((y, x))
                bfs()
                
    answer = max(answer, color - 101)
    
print(answer)
