def spread(y, x):
    count = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= c or ny < 0 or ny >= r or room[ny][nx] == -1:
            continue
        
        change[ny][nx] += room[y][x] // 5
        count += 1
        
    room[y][x] -= (room[y][x] // 5) * count
    
def circulate(position, isUp):
    y, x = position, 1
    
    if isUp:
        # 반시계 방향 순환
        temp1 = room[y][x]
        room[y][x] = 0
        while x < c - 1:
            x += 1
            temp2 = room[y][x]
            room[y][x] = temp1
            temp1 = temp2
            
        while y > 0:
            y -= 1
            temp2 = room[y][x]
            room[y][x] = temp1
            temp1 = temp2
            
        while x > 0:
            x -= 1
            temp2 = room[y][x]
            room[y][x] = temp1
            temp1 = temp2
            
        # 공기청정기쪽으로 이동한 미세먼지는 삭제
        while y < position:
            y += 1
            temp2 = room[y][x]
            if y != position:
                room[y][x] = temp1
            temp1 = temp2
            
    else:
        # 시계 방향 순환
        temp1 = room[y][x]
        room[y][x] = 0
        while x < c - 1:
            x += 1
            temp2 = room[y][x]
            room[y][x] = temp1
            temp1 = temp2
            
        while y < r - 1:
            y += 1
            temp2 = room[y][x]
            room[y][x] = temp1
            temp1 = temp2
            
        while x > 0:
            x -= 1
            temp2 = room[y][x]
            room[y][x] = temp1
            temp1 = temp2
        
        # 공기청정기쪽으로 이동한 미세먼지는 삭제
        while y > position:
            y -= 1
            temp2 = room[y][x]
            if y != position:
                room[y][x] = temp1
            temp1 = temp2

r, c, t = map(int, input().split())
room = []
for _ in range(r):
    room.append(list(map(int, input().split())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
purifiers = []
time = 0

# 공기 첫번째 위치 판별 (첫 번째가 위쪽 공기청정기, 두 번째가 아래쪽 공기청정기)
for row in range(len(room)):
    if room[row][0] == -1:
        purifiers.append(row)

while time < t:
    change = [[0] * c for _ in range(r)]
    
    # 공기를 확산시킴
    for y in range(len(room)):
        for x in range(len(room[y])):
            if room[y][x] > 0:
                spread(y, x)
                
    # 변경사항 반영            
    for y in range(len(change)):
        for x in range(len(change[y])):
            if change[y][x] > 0:
                room[y][x] += change[y][x]
        
    # 공기청정기 가동
    circulate(purifiers[0], True)
    circulate(purifiers[1], False)
        
    time += 1
        
# 시간이 지나고 남은 미세먼지의 양 출력
print(sum(map(sum, room)) + 2)
