n = int(input())
numbers = list(map(int, input().split()))

dp = [0] * n
for i in range(n):
    cnt = 0
    for j in range(i):
        if numbers[i] > numbers[j]:
            cnt = max(cnt, dp[j])
    dp[i] = cnt + 1

print(max(dp))
