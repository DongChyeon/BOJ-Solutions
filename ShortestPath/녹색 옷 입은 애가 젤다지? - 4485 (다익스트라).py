import heapq

def dijkstra(start_x, start_y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    heap = []
    heapq.heappush(heap, (field[start_x][start_y], start_x, start_y))
    
    while heap:
        dist, x, y = heapq.heappop(heap)
        
        if distance[x][y] < dist:
            continue
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + field[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(heap, (cost, nx, ny))
    
INF = int(10e9)
count = 0

while True:
    count += 1
    n = int(input())
    
    if n == 0:
        break
    
    distance = [[INF for _ in range(n)] for _ in range(n)]
    field = [list(map(int, input().split())) for _ in range(n)]
    
    dijkstra(0, 0)
    
    print("Problem %d: %d" % (count, distance[n - 1][n - 1]))
