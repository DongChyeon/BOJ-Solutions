# 포인트
# 1. 정렬을 이용해 가장 위쪽, 가장 왼쪽 먹을 수 있는 물고기를 탐색
# 2. 물고기를 먹었을 때의 시간 저장
# 3. 물고기를 먹었을 때 queue, visited를 초기화

from collections import deque

def bfs(start_y, start_x):
    queue, visited = deque([(start_y, start_x)]), [(start_y, start_x)]
    time = 0
    # 아기 상어의 크기와 물고기를 먹은 수
    size, count = 2, 0
    eat_flag = False
    answer = 0
    
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    
    while queue:
        # 가장 위 (y가 작은 순), 가장 왼쪽 (x가 작은 순)을 탐색하기 위해 정렬
        queue = deque(sorted(queue))
        for _ in range(len(queue)):
            y, x = queue.popleft()
            # 물고기가 아기 상어의 크기보다 작다면 잡아 먹음
            if fishbowl[y][x] != 0 and fishbowl[y][x] < size:
                fishbowl[y][x] = 0
                count += 1
                
                # 아기 상어의 크기만큼 잡아먹는다면 크기를 늘려줌
                if count == size:
                    size += 1
                    count = 0
                    
                # 잡아먹은 경우 queue, visited 초기화
                queue, visited = deque(), [(y, x)]
                eat_flag = True
                
                # 잡아먹었을 때의 시간 기억
                answer = time
                
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                # 범위를 벗어났거나 방문했을 경우 스킵
                if nx < 0 or nx >= n or ny < 0 or ny >= n or (ny, nx) in visited:
                    continue
                if fishbowl[ny][nx] <= size:
                    queue.append((ny, nx))
                    visited.append((ny, nx))
            
            # 물고기를 잡아먹은 경우 반복문을 계속 진행할 필요 없음
            if eat_flag:
                eat_flag = False
                break
            
        time += 1
            
    print(answer)

n = int(input())
fishbowl = [list(map(int, input().split())) for _ in range(n)]

for y in range(len(fishbowl)):
    for x in range(len(fishbowl[y])):
        if fishbowl[y][x] == 9:
            fishbowl[y][x] = 0
            bfs(y, x)
            break
    if 9 in fishbowl[y]:
        break
