n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    # 이전에 있는 집과 다른색으로 칠함
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])
    
print(min(dp[n - 1]))
