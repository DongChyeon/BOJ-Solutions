from collections import deque

def bfs(start):
    queue = deque([(start, 0)])
    visited = [False] * (n + 1)
    
    visited[start] = True
    while queue:
        b, cost = queue.popleft()
        for node in tree[b]:
            a, c = node
            if not visited[a]:
                distances[a] = cost + c 
                visited[a] = True
                queue.append((a, distances[a]))

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))
    
# 아무 노드에서 가장 거리가 먼 노드를 구하고
# 해당 노드에서 가장 거리가 먼 노드를 계산
distances = [0] * (n + 1)
bfs(1)
farthest_node = distances.index(max(distances))

distances = [0] * (n + 1)
bfs(farthest_node)
print(max(distances))
