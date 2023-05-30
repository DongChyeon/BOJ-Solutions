# dp[i] = 높이 i가 되기 위한 최소 노드 수수
dp = [0] * 44
dp[0], dp[1], dp[2] = 0, 1, 2
for i in range(3, 44):
    dp[i] = dp[i - 1] + dp[i - 2] + 1

t = int(input())
for _ in range(t):
    v = int(input())
    idx = 0
    while idx < 44:
        if dp[idx + 1] > v:
            break
        idx += 1
    print(idx)
