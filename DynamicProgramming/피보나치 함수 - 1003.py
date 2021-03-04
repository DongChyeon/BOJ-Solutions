t = int(input())
dp = [0] * 41

# dp 테이블 생성
dp[0] = (1, 0)
dp[1] = (0, 1)

for _ in range(t):
    n = int(input())
    for i in range(2, n + 1):
        # -1한 값과 -2한 값의 트리를 가지게 됨
        dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])
    print(dp[n][0], dp[n][1])