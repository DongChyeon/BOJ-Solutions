import sys
from collections import deque

def bfs():
    global answer
    
    dx = [1, -1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, 1, -1, -1, -1, 1, 1]
    
    while queue:
        y, x = queue.popleft()
        
        # 상하좌우 대각선을 탐색해 땅일 0으로 처리
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= w or ny < 0 or ny >= h or field[ny][nx] == 0:
                continue
            if field[ny][nx] == 1:
                field[ny][nx] = 0
                queue.append((ny, nx))
            
    answer += 1

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    field = [list(map(int, input().split())) for _ in range(h)]
    answer = 0
    queue = deque()
    
    for y in range(h):
        for x in range(w):
            if field[y][x] == 1:
                queue.append((y, x))
                field[y][x] = 0
                bfs()
                
    print(answer)
