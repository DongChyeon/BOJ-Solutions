def dfs(level, numbers):
    if level == k + 1:
        answer.append(numbers)
        return
    
    for current in range(10):
        if promising(level, current, numbers):
            visited[current] = True
            dfs(level + 1, numbers + str(current))
            visited[current] = False
        
def promising(level, current, numbers):
    if level == 0:
        return True
        
    if not visited[current]:
        if data[level - 1] == '<':
            # 현재 선택한 수가 이전 수보다 커야함
            if current > int(numbers[-1]):
                return True
        elif data[level - 1] == '>':
            # 현재 선택한 수가 이전 수보다 작아야 함
            if current < int(numbers[-1]):
                return True
        
    return False

k = int(input())
data = list(input().split())
visited = [False] * 10
answer = []

dfs(0, '')
answer.sort()

# 최대, 최소 정수를 출력력
print(answer[-1])
print(answer[0])
