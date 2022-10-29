import copy

def dfs(depth, room):
    global answer
    
    if depth == len(cctv_list):
        answer = min(answer, sum(x.count(0) for x in room))
        return
    room_copy = copy.deepcopy(room)
    num, x, y = cctv_list[depth]
    for direction in cctv_direction[num]:
        check(num, x, y, direction, room_copy)
        dfs(depth + 1, room_copy)
        room_copy = copy.deepcopy(room) # cctv를 다른 방향으로 해서 재탐색

def check(num, x, y, direction, room):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 > nx or nx >= m or 0 > ny or ny >= n:
                break
            if room[ny][nx] == 6:
                break
            elif room[ny][nx] == 0:
                room[ny][nx] = '#'

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
answer = n * m
cctv_list = []

for y in range(n):
    for x in range(m):
        if room[y][x] >= 1 and room[y][x] <= 5:
            cctv_list.append((room[y][x], x, y))

dx = [0, 0, -1, 1]  # 0 : up / 1 : down / 2 : left / 3 : right
dy = [-1, 1, 0, 0]

# cctv 번호별 식별 가능 방향
cctv_direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

dfs(0, room)
    
print(answer)
