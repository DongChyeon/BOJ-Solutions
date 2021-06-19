def dijkstra(start, end, n):
    queue = []
    distance = [INF] * (n + 1)
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
                
    return distance[end]

import sys
import heapq

input = sys.stdin.readline
INF = int(10e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

pos1, pos2 = map(int, input().split())

# 두가지의 경우
# start -> pos1 -> pos2 -> end
# start -> pos2 -> pos1 -> end

# 1번 정점에서 거쳐야 하는 첫번째 정점까지의 거리, 두번째 정점까지의 거리
start_to_pos1, start_to_pos2 = dijkstra(1, pos1, n), dijkstra(1, pos2, n)

# 거쳐야 하는 첫번째 정점부터 거쳐야 하는 두번째 정점까지의 거리
pos1_to_pos2 = dijkstra(pos1, pos2, n)

# 거쳐야 하는 첫번째 정점에서 N번째 정점까지의 거리
pos1_to_end = dijkstra(pos1, n, n)

# 거쳐야 하는 두번째 정점에서 N번째 정점까지의 거리
pos2_to_end = dijkstra(pos2, n, n)

answer = min(start_to_pos1 + pos1_to_pos2 + pos2_to_end, start_to_pos2 + pos1_to_pos2 + pos1_to_end)
if answer >= INF:
    print(-1)
else:
    print(answer)
