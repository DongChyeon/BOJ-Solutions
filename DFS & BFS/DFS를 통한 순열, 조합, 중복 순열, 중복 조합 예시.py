''' dfs를 통한 순열 구하기
def dfs(level):
    if level == m:
        print(result)
        return
    for i in range(n):
        if visited[i] == True:
            continue
        result[level] = data[i]
        visited[i] = True
        dfs(level + 1)
        visited[i] = False
        
n, m = map(int, input().split())        
data = [i + 1 for i in range(n)]
result = [0] * m
visited = [False] * n
dfs(0)
'''

''' dfs를 통한 조합 구하기
def dfs(level, start):
    if level == m:
        print(result)
        return
    for i in range(start, n):
        result[level] = data[i]
        dfs(level + 1, i + 1)
        
n, m = map(int, input().split())
data = [i + 1 for i in range(n)]
result = [0] * m
dfs(0, 0)
'''

''' dfs를 통한 중복 순열 구하기
def dfs(count):
    if count == m:
        print(result)
        return
    for i in range(1, n + 1):
        result.append(i)
        dfs(count + 1)
        result.pop()

n, m = map(int, input().split())
result = []
dfs(0)
'''

''' dfs를 통한 중복 조합 구하기
def dfs(idx, count):
    if count == m:
        print(result)
        return
    for i in range(idx, n):
        result.append(i + 1)
        dfs(i, count + 1)
        result.pop()
        
n, m = map(int, input().split())
result = []
dfs(0, 0)
'''
