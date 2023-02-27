from collections import deque

def pour(x, y, z):
    if not visited[x][y][z]:
        visited[x][y][z] = True
        queue.append((x, y, z))

def bfs():
    while queue:
        x, y, z = queue.popleft()
        
        if x == 0:
            answer.append(z)
        
        # x -> y    
        water = min(x, b - y)
        pour(x - water, y + water, z)
        # x -> z
        water = min(x, c - z)
        pour(x - water, y, z + water)
        # y -> x
        water = min(y, a - x)
        pour(x + water, y - water, z)
        # y -> z
        water = min(y, c - z)
        pour(x, y - water, z + water)
        # z -> x
        water = min(z, a - x)
        pour(x + water, y, z - water)
        # z -> y
        water = min(z, b - y)
        pour(x, y + water, z - water)

a, b, c = map(int, input().split())

# 물통에 있는 물의 양을 상태 배열로 봄
visited = [[[False] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)]

answer = []
queue = deque([(0, 0, c)])
visited[0][0][c] = True
bfs()

for x in sorted(answer):
    print(x, end = ' ')
