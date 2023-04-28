t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    visited = [0] * (n + 1)
    
    flag = True
    for v in range(1, n + 1):
        if not visited[v]:
            stack = [(v, 1)]
            
            while stack:
                current, color = stack.pop()
                if visited[current] and visited[current] != color:
                    flag = False   
                    break
                visited[current] = color
                # 인접한 노드 중 방문 못한 노드는 다른 색으로 칠함
                for n in graph[current]:
                    if not visited[n]:
                        stack.append((n, -color))
    
    if flag:
        print('possible')
    else:
        print('impossible')
