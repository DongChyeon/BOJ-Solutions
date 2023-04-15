a, b, c = map(int, input().split())
x_str = list(input())
y_str = list(input())

dp = [[0 for _ in range(len(x_str) + 1)] for _ in range(len(y_str) + 1)]
for y in range(1, len(y_str) + 1):
    dp[y][0] = dp[y - 1][0] + b
for x in range(1, len(x_str) + 1):
    dp[0][x] = dp[0][x - 1] + b
    
for y in range(1, len(y_str) + 1):
    for x in range(1, len(x_str) + 1):
        temp = dp[y - 1][x - 1] + a if (x_str[x - 1] == y_str[y - 1]) else dp[y - 1][x - 1] + c
        
        dp[y][x] = max(dp[y - 1][x] + b, dp[y][x - 1] + b, temp)
    
print(dp[y][x])
