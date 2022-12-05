n = int(input())
time_table = [[0, 0]]
for _ in range(n):
    time_table.append(list(map(int, input().split())))

dp = [0] * (n + 2)
for i in range(1, n + 2):
    dp[i] = max(dp[i - 1], dp[i])
    if i > n:
        continue
    day = time_table[i][0] + i
    if day > n + 1:
        continue
    if dp[day] < dp[i] + time_table[i][1]:
        dp[day] = dp[i] + time_table[i][1]
    
print(dp[n + 1])
