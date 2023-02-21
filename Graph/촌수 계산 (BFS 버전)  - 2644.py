from collections import deque
import heapq

def bfs(start):
    queue = deque([start])
    distance[start] = 0
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            # 방문한 적이 없는 곳이라면 거리 갱신신
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)

print(distance[b])
