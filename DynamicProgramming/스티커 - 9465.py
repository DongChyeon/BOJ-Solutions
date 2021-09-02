t = int(input())
for _ in range(t):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    
    if n > 1:
        # 왼쪽 대각선 아래의 스티커 선택
        dp[0][1] += dp[1][0]
        # 왼쪽 대각선 위의 스티커 선택
        dp[1][1] += dp[0][0]
        
        for i in range(2, n):
            # 왼쪽 대각선 아래의 스티커 선택 또는 그 왼쪽의 스티커 선택
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            # 왼쪽 대각선 위의 스티커 선택 또는 그 왼쪽의 스티커 선택
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
        
    print(max(dp[0][n - 1], dp[1][n - 1]))
