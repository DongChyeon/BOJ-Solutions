n = int(input())
cards = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = cards[0]

for i in range(2, n + 1):
    dp[i] = dp[i - 1]
    for j in range(n):
        if i - (j + 1) < 0:
            continue
        # 해당 카드를 구매했을 때 가격이 더 비싸다면 갱신
        if dp[i - (j + 1)] + cards[j] > dp[i]:
            dp[i] = dp[i - (j + 1)] + cards[j]
        
print(dp[n])
