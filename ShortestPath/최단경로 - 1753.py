import sys
import heapq

input = sys.stdin.readline
INF = int(10e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
# 다익스트라 알고리즘으로 각 정점까지의 최단거리를 구함
queue = []
heapq.heappush(queue, (0, start))
distance[start] = 0
while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0]))
            
for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
