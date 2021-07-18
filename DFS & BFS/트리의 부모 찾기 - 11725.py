import sys

def find_parent(node):
    # 부모 노드 방문 표시
    visited[node] = True
    
    for x in tree[node]:
        # 연결된 노드 중 방문 표시가 안되있다면 자식 노드
        if not visited[x]:
            parent[x] = node
            find_parent(x)

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
parent = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
find_parent(1)
    
for i in range(2, n + 1):
    print(parent[i])
