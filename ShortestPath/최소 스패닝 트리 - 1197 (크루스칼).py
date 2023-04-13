import heapq

def find_parent(parent, edge):
    if parent[edge] != edge:
        parent[edge] = find_parent(parent, parent[edge])
    
    return parent[edge]
    
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(heap):
    parent = [i for i in range(v + 1)]
    
    result = 0
    
    while heap:
        cost, a, b = heapq.heappop(heap)
        
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
                
    return result

v, e = map(int, input().split())
heap = []

for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(heap, (c, a, b))

print(kruskal(heap))
