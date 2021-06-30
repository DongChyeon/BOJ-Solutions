from collections import deque

def bfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    queue = deque([v])
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * len(graph)
bfs(graph, 1, visited)

result = 0
for i in range(2, len(graph)):
    if visited[i] == True:
        result += 1
        
print(result)
