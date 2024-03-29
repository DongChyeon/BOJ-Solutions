import heapq
import sys
INF = int(10e9)

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append((y, 1))
    graph[y].append((x, 1))

def dijkstra(start):
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
                
dijkstra(a)

if distance[b] == INF:
    print(-1)
else:
    print(distance[b])
