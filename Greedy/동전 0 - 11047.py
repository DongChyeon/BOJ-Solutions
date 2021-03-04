n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.insert(0, int(input()))
result = 0

for i in range(len(coins)):
    # 가장 큰 단위의 동전부터 차례차례 사용
    if coins[i] <= k:
        result += k // coins[i] 
        k %= coins[i]
    
print(result)
