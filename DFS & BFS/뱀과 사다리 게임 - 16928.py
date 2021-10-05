from collections import deque

def bfs():
    queue = deque([(1, 0)])
    visited = [False] * 101
    
    while queue:
        pos, count = queue.popleft()
        visited[pos] = True
        
        if pos == 100:
            print(count)
            break
        
        # 주사위를 1부터 6까지 굴림
        for dx in range(1, 7):
            npos = pos + dx
            # 범위를 초과할 경우 스킵
            if npos < 1 or npos > 100 or visited[npos]:
                continue
            # 사다리를 만날 경우 이동
            for x, y in ladders:
                if npos == x:
                    npos = y
                    break
            # 뱀을 만날 경우 이동
            for x, y in snakes:
                if npos == x:
                    npos = y
                    break
            queue.append((npos, count + 1))

n, m = map(int, input().split())
ladders = [list(map(int, input().split())) for _ in range(n)]
snakes = [list(map(int, input().split())) for _ in range(m)]

bfs()
