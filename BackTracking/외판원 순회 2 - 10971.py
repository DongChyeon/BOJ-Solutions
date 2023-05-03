def dfs(start, level, cost):
    global answer
    
    # 모든 도시를 방문했고 다시 출발지점으로 돌아올 수 있다면 정답 갱신
    if level == n:
        if graph[start][0]:
            answer = min(answer, cost + graph[start][0])
        return
        
    for end in range(n):
        if promising(start, end):
            if cost + graph[start][end] < answer:
                visited[end] = True
                dfs(end, level + 1, cost + graph[start][end])
                visited[end] = False
                 
# 방문하지 않은 도시이고 현재 도시에서 방문할 수 있는 길이 있을 때때
def promising(start, end):
    if not visited[end] and graph[start][end]:
        return True
    else:
        return False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
visited[0] = True
answer = int(10e9)

dfs(0, 1, 0)

print(answer)
