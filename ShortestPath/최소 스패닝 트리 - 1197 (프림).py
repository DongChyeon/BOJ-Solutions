import heapq

def prim(start_edge):
    result = 0
    
    visited = [False] * (v + 1)
    
    heap = []
    heapq.heappush(heap, (0, start_edge))
    
    while heap:
        cost, edge = heapq.heappop(heap)
        
        if visited[edge]:
            continue
        visited[edge] = True
        
        result += cost
        
        for e, c in graph[edge]:
            if not visited[e]:
                heapq.heappush(heap, (c, e))
                
    return result

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(prim(1))
