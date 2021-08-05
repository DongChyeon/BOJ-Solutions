INF = int(10e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 모든 지점에서 다른 모든 지점까지의 최단 경로를 구함 - 플로이드 워셜 알고리즘 이용
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 케빈 베이컨의 수가 가장 낮은 사람을 찾음
answer = 1
kevin_bacon_number = sum(x if x != INF else 0 for x in graph[1])
for i in range(2, len(graph)):
    temp = sum(x if x != INF else 0 for x in graph[i])
    if temp < kevin_bacon_number:
        kevin_bacon_number = temp
        answer = i

print(answer)
