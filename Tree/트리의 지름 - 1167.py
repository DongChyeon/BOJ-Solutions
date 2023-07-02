def dfs(start):
    stack = [(start, 0)]
    visited[start] = True
    
    while stack:
        dest, cost = stack.pop()
        for node in tree[dest]:
            d, c = node
            if not visited[d]:
                visited[d] = True
                distances[d] = cost + c
                stack.append((d, distances[d]))

v = int(input())
tree = [[] for _ in range(v + 1)]
for _ in range(v):
    temp = list(map(int, input().split()))
    dest = temp[0]
    idx = 1
    while temp[idx] != -1:
        tree[dest].append((temp[idx], temp[idx + 1]))
        idx += 2

distances = [0] * (v + 1)
visited = [False] * (v + 1)
dfs(1)

farthest_node = distances.index(max(distances))
distances = [0] * (v + 1)
visited = [False] * (v + 1)
dfs(farthest_node)
print(max(distances))
