from collections import deque

def bfs():
    global answer
    
    while queue:
        pos, count = queue.popleft()
        dy = [pos + u, pos - d]
        
        if pos == g:
            answer = min(answer, count)
            return
            
        for pos in dy:
            if pos < 1 or pos > f or visited[pos]:
                continue
            queue.append((pos, count + 1))
            visited[pos] = True
        
f, s, g, u, d = map(int, input().split())
visited = [False] * (f + 1)
visited[s] = True
answer = int(10e9)
queue = deque([(s, 0)])
bfs()

if answer == int(10e9):
    print('use the stairs')
else:
    print(answer)
