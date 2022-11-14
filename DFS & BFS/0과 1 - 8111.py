from collections import deque

def bfs(num):
    # 오버 플로우를 방지하기 위해 문자형으로 원래 숫자도 저장
    queue = deque([(1, '1')])
    visited = [False] * 20001
    visited[1] = True
    
    while queue:
        cur_num, cur_str = queue.popleft()
        if cur_num == 0:
            return cur_str
        if len(cur_str) > 100:
            return 'BRAK'
        # x modular n은 (x modular n) modular n과 같음
        if not visited[(cur_num * 10) % num]:
            visited[(cur_num * 10) % num] = True
            queue.append(((cur_num * 10) % num, cur_str + '0'))
        if not visited[(cur_num * 10 + 1) % num]:
            visited[(cur_num * 10 + 1) % num] = True
            queue.append(((cur_num * 10 + 1) % num, cur_str + '1'))
    
    return 'BRAK'

n = int(input())
for _ in range(n):
    print(bfs(int(input())))
