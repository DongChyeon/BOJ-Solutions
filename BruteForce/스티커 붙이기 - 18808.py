n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]

def rotate(sticker):
    row, col = len(sticker), len(sticker[0])
    new_sticker = [[0 for _ in range(row)] for _ in range(col)]
    
    for y in range(row):
        for x in range(col):
            new_sticker[x][row - y - 1] = sticker[y][x]
            
    return new_sticker

def is_attachable(start_x, start_y, sticker):
    row, col = len(sticker), len(sticker[0])
    for y in range(start_y, start_y + row):
        for x in range(start_x, start_x + col):
            if y >= n or x >= m:
                return False
            if sticker[y - start_y][x - start_x] == 1 and board[y][x] != 0:
                return False
    
    return True
    
def attach_sticker(start_x, start_y, sticker):
    row, col = len(sticker), len(sticker[0])
    for y in range(start_y, start_y + row):
        for x in range(start_x, start_x + col):
            if sticker[y - start_y][x - start_x] == 1:
                board[y][x] = 1

for _ in range(k):
    # 1. 스티커를 회전시키지 않고 모눈종이에서 떼어낸다.
    # 2. 다른 스티커와 겹치거나 노트북을 벗어나지 않으면서 스티커를 붙일 수 있는 위치를 찾는다. 혜윤이는 노트북의 위쪽부터 스티커를 채워 나가려고 해서, 스티커를 붙일 수 있는 위치가 여러 곳 있다면 가장 위쪽의 위치를 선택한다. 가장 위쪽에 해당하는 위치도 여러 곳이 있다면 그중에서 가장 왼쪽의 위치를 선택한다.
    # 3. 선택한 위치에 스티커를 붙인다. 만약 스티커를 붙일 수 있는 위치가 전혀 없어서 스티커를 붙이지 못했다면, 스티커를 시계 방향으로 90도 회전한 뒤 2번 과정을 반복한다.
    # 4. 위의 과정을 네 번 반복해서 스티커를 0도, 90도, 180도, 270도 회전시켜 봤음에도 스티커를 붙이지 못했다면 해당 스티커를 붙이지 않고 버린다.
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    
    attach_flag = False
    for _ in range(4):
        # 스티커를 붙였으면 반복문 탈출
        if attach_flag == True:
            break
        # 가장 왼쪽 위부터 탐색
        for y in range(n):
            if attach_flag == True:
                break
            for x in range(m):
                # 스티커를 붙일 수 있다면 붙임
                if is_attachable(x, y, sticker):
                    attach_sticker(x, y, sticker)
                    attach_flag = True
                    break
        # 스티커를 붙이지 못했다면 스티커를 회전시킴
        if attach_flag == False:
            sticker = rotate(sticker)
    
answer = 0
for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            answer += 1

print(answer)
