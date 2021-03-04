n = int(input())
dp = [0] * 1000001

dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    # i - 1일 때 1 타일을 붙이는 경우와 i - 2일 때 00 타일을 붙이는 경우
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])