INF = int(10e9)

def bellman_ford(start):
    distances = [INF] * (n + 1)
    distances[start] = 0
    
    # 정점의 개수 - 1 만큼 반복문을 돌고나면 최단거리가 완성됨
    # 하지만 여기서 한 번 더 돌렸을 때 최단거리가 갱신된다면 음의 사이클이 존재한다는 의미미
    for i in range(n):
        for a, b, c in edges:
            if distances[a] == INF:
                continue
            
            if distances[b] > distances[a] + c:
                if i == n - 1:
                    return [-1]
                
                distances[b] = distances[a] + c
        
    return distances

n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

distances = bellman_ford(1)

if len(distances) == 1 and distances[0] == -1:
    print(-1)
else:
    for i in range(2, len(distances)):
        print(-1 if distances[i] == INF else distances[i])
