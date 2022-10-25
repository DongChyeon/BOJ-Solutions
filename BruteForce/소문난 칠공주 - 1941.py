from collections import deque
from itertools import combinations

def bfs(field):
    global answer
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    cnt = 0
    while queue:
        y, x = queue.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or field[ny][nx] == True:
                continue
            
            if field[ny][nx] == False:
                field[ny][nx] = True
                queue.append((ny, nx))
        
        # 7명이 모두 인접해있으면 경우의 수 추가
        if cnt == 7:
            answer += 1
            return

data = [list(input()) for _ in range(5)]

cases = []
for i in range(5):
    for j in range(5):
        cases.append((i, j))

# 7명을 골라 이다솜파가 우위를 점하는 경우를 check에 담음
check = []       
for comb in list(combinations(cases, 7)):
    s_cnt, y_cnt = 0, 0
    for x in comb:
        if data[x[0]][x[1]] == 'S':
            s_cnt += 1
        elif data[x[0]][x[1]] == 'Y':
            y_cnt += 1
    if s_cnt > y_cnt:
        check.append(comb)

# bfs를 통해 서로 인접해있는지 확인
answer = 0
for comb in check:
    field = [[True] * 5 for _ in range(5)]
    queue = deque([(comb[0][0], comb[0][1])])
    
    for i in range(1, 7):
        field[comb[i][0]][comb[i][1]] = False
    bfs(field)

print(answer)
