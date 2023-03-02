from itertools import permutations
from collections import deque

def is_correct(numbers):
    if numbers == '123456780':
        return True
    else:
        return False

def bfs(start, visited):
    answer = []
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    queue = deque([(start, 0)])
    
    while queue:
        numbers, count = queue.popleft()
        visited[numbers] = True
        
        if is_correct(numbers):
            return count
            
        pos = numbers.index('0')
        y, x = pos // 3, pos % 3
        
        # 0 주변에 숫자가 존재할 경우 위치를 바꿈꿈
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if 0 <= ny < 3 and 0 <= nx < 3:
                npos = 3 * ny + nx
                new_numbers = list(numbers)
                new_numbers[pos], new_numbers[npos] = new_numbers[npos], new_numbers[pos]
                new_numbers = ''.join(new_numbers)
                
                if not visited[new_numbers]:
                    queue.append((new_numbers, count + 1))
                
    return -1

field = [list(map(int, input().split())) for _ in range(3)]

# 방문 정보 초기화
# 숫자 배열 자체를 방문 가능한 값으로 봄
visited = dict()
for x in permutations([1, 2, 3, 4, 5, 6, 7, 8, 0], 9):
    visited[''.join(map(str, x))] = False
    
start = ''.join([str(item) for innerList in field for item in innerList])

print(bfs(start, visited))
