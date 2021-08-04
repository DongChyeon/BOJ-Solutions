import sys

input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

# 이분 탐색을 통해 절단할 높이를 찾아냄
while start <= end:
    mid = (start + end) // 2
    total = sum(x - mid if x > mid else 0 for x in trees)
    
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        
print(start - 1)
