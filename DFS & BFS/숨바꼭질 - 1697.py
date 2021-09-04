from collections import deque

def bfs():
    while queue:
        pos, count = queue.popleft()
        visited[pos] = True
        
        dx = [pos + 1, pos - 1, 2 * pos]
        
        # 동생이 있는 위치에 도달하면 도달 시간 출력
        if pos == k:
            print(count)
            return
        
        for pos in dx:
            # 범위를 벗어나거나 방문했을 경우 스킵
            if pos < 0 or pos > 100000 or visited[pos] == True:
                continue
            queue.append((pos, count + 1))

n, k = map(int, input().split())
visited = [False] * 100001
queue = deque([(n, 0)])

bfs()
