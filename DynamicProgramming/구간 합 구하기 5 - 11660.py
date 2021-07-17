import sys

input = sys.stdin.readline
n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for row in data:
    for i in range(1, n):
        row[i] += row[i - 1]
    
# 부분합을 이용해 풀이
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0
    
    for i in range(x1 - 1, x2):
        if y1 == 1:
            answer += data[i][y2 - 1]
        else:
            answer += data[i][y2 - 1] - data[i][y1 - 2]
    
    print(answer)
