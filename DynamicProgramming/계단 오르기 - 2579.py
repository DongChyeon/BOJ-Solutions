n = int(input())
dp = [0] * n
stair = []

for _ in range(n):
    stair.append(int(input()))
    
if n < 3:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = max(dp[0] + stair[1], stair[1])
    dp[2] = max(dp[0] + stair[2], stair[1] + stair[2])
    for i in range(3, n):
        # 연속된 세 개의 계단을 밟으면 안됨
        # i - 3, i - 1, i번째 계단을 밟은 경우 / i - 2, i번째 계단을 밟은 경우
        dp[i] = max(stair[i] + stair[i - 1] + dp[i - 3], stair[i] + dp[i - 2])
        
    print(dp[n - 1])
