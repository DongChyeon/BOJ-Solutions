INF = int(10e9)

n = int(input())
graph = []
            
# 입력받은 인접행렬로 그래프 초기화
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# 0일 경우 거리를 INF로 설정
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF
            
# 플로이드 워셜 알고리즘 이용            
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 거리가 INF(닿을 수 없음)이 아닐 경우 1 출력            
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
