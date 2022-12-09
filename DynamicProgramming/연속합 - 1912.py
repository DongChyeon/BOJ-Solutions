n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    # 이전 값이 음수거나 더해서 음수면은 더할 필요 없음
    if dp[i - 1] < 0 or dp[i - 1] + dp[i] < 0:
        continue
    dp[i] += dp[i - 1]
    
print(max(dp))
