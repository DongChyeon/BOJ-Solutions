import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap:
        # 가장 최단거리가 짧은 노드 선택
        dist, now = heapq.heappop(heap)
        # 이미 갱신한 값일 경우 무시
        if distance[now] < dist:
            continue
        # 선택된 노드와 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 선택된 노드를 거쳐서 이동하는 경우가 더 빠르면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

n, m, x = map(int, input().split())
INF = int(10e9)
path = []

for _ in range(m):
    a, b, c = map(int, input().split())
    path.append((a, b, c))

# 각 학생들이 x 마을로 가는 거리는 단방향 도로의 방향을 거꾸로 함으로써 구함
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in path:
    graph[i[1]].append((i[0], i[2]))
    
dijkstra(x)
go = distance[1:]

# x 마을로부터 각 학생들이 집에 오는 거리를 구함
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in path:
    graph[i[0]].append((i[1], i[2]))

dijkstra(x)
come = distance[1:]

# 오고 가는 거리가 가장 오래 걸리는 학생을 출력
print(max([go[i] + come[i] for i in range(len(go))]))
