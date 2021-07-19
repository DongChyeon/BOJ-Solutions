import sys

input = sys.stdin.readline
n, k = map(int, input().split())
goods = [[0, 0]]

for _ in range(n):
    w, v = map(int, input().split())
    # (물건의 무게, 물건의 가치)
    goods.append((w, v))
    
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

# i번째까지 물건을 선택 가능했을 때
for i in range(n + 1):
    # j만큼 가방에 넣을 수 있을 때
    for j in range(k + 1):
        if goods[i][0] <= j:
            # i번째 물품 + i - 1번째 물품까지 선택할 수 있고 j - 현재 물품의 무게만큼 들 수 있을 때
            # i - 1번째 물품까지 선택할 수 있고 j 만큼 들 수 있을 때를 비교
            dp[i][j] = max(goods[i][1] + dp[i - 1][j - goods[i][0]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
            
print(dp[-1][-1])
