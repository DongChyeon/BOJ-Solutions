n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))
dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    for j in range(coin[i], k + 1):
        dp[j] += dp[j - coin[i]]

print(dp[k])
