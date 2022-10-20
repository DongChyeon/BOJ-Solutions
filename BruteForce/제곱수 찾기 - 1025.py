import math

n, m = map(int, input().split())
data = [[num for num in input()] for _ in range(n)]
answer = -1

for y in range(n):
    for x in range(m):
        for dy in range(-n, n):
            for dx in range(-m, m):
                if dx == 0 and dy == 0:
                    continue
                num = ""
                nx, ny = x, y
                while True:
                    if nx < 0 or nx > m - 1 or ny < 0 or ny > n - 1:
                        break
                    num += data[ny][nx]
                    if math.sqrt(int(num)) % 1 == 0 and int(num) > answer:
                        answer = int(num)
                    nx, ny = nx + dx, ny + dy
                
print(answer)
