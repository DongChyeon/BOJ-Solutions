import sys

input = sys.stdin.readline
k, n = map(int, input().split())
lines = []

for _ in range(k):
    lines.append(int(input()))
    
# start를 0으로 할 시 ZeroDividsionError 발생
# 예를 들어 1 1 \n 1을 입력했을 시
start, end = 1, max(lines)

# 이분 탐색을 통해 절단할 길이를 찾아냄
while start <= end:
    mid = (start + end) // 2
    total = sum(x // mid for x in lines)
    
    if total < n:
        end = mid - 1
    else:
        start = mid + 1
        
print(start - 1)
