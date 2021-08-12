n = int(input())
schedule = [(0, 0)]
dp = [0] * (n + 1)

for i in range(1, n + 1):
    time, pay = map(int, input().split())
    schedule.append((time, pay))

    dp[i] = pay
    
for i in range(2, n + 1):
    for j in range(1, i):
        # max(i일에 상담하면 얻는 이득 + 1~j일까지의 이익, i일까지의 이익) 
        if i - j >= schedule[j][0]:
            dp[i] = max(schedule[i][1] + dp[j], dp[i])

answer = 0

for i in range(1, n + 1):
    # n + 1일 이후에 상담이 끝나는 경우는 제외
    if i + schedule[i][0] <= n + 1:
        answer = max(answer, dp[i])
        
print(answer)
