def dfs(at, depth):
    # m 만큼 pool에 숫자가 담기게 된다면 출력
    if depth == m:
        for x in pool:
            print(x, end=' ')
        print()
        return
    
    # 이전에 넣은 숫자보다 큰 수를 탐색
    for i in range(at, n + 1):
        pool[depth] = i
        dfs(i + 1, depth + 1)

n, m = map(int, input().split())
pool = [0 for x in range(m)]
dfs(1, 0)