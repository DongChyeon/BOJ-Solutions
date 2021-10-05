t = int(input())
dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11):
    # i - 3에 3을 더하는 경우의 수, i - 2에 2을 더하는 경우의 수, i - 1에 1을 더하는 경우의 수
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    
for _ in range(t):
    print(dp[int(input())])
