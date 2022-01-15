INF = int(10e9)
n, m, r = map(int, input().split())
items = [int(x) for x in input().split()]
graph = [[INF] * (n + 1) for _ in range(n + 1)]
answer = 0

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
    
for _ in range(r):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
    if graph[b][a] > c:
        graph[b][a] = c

# 플로이드 와샬 알고리즘을 통해 지역간의 최소 거리를 구함        
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# i 지역을 시작점으로 잡았을 때 탐색 범위 m 안에 있는 경우를 계산
for i in range(1, n + 1):
    value = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF and graph[i][j] <= m:
            value += items[j - 1]
    
    answer = max(answer, value)

print(answer)
