INF = int(1e9)

n = int(input())
distances = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    distances[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    distances[a - 1][b - 1] = 1
    distances[b - 1][a - 1] = 1
    
for k in range(n):
    for a in range(n):
        for b in range(n):
            if distances[a][b] > distances[a][k] + distances[k][b]:
                distances[a][b] = distances[a][k] + distances[k][b]

scores = [max(distances[i]) for i in range(n)]
leader_score = min(scores)

candidates = []
for i, score in enumerate(scores):
    if score == leader_score:
        candidates.append(i + 1)
        
print(leader_score, len(candidates))
print(' '.join(map(str, candidates)))
