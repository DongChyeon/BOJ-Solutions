import sys

input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
# 구간 합을 기억할 dp 테이블 생성
dp = [0]

for i in range(n):
    dp.append(dp[i] + data[i])
    
for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])
