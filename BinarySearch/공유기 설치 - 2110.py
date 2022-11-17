# 찾고자 하는 값보다 큰 값이 처음 나타나는 위치를 구함
def upper_bound(target):
    # 큰 값이 처음 나오는 위치이므로 end = 최대거리 + 1
    start, end = 1, pos[-1] - pos[0] + 1
    
    while start < end:
        mid = (start + end) // 2
        
        # 설치 가능한 공유기 개수가 더 적다면 end를 줄임
        if target > installable_routers(mid):
            end = mid
        else:
            start = mid + 1
            
    return start

def installable_routers(dist):
    count = 1
    last_idx = 0
    
    for i in range(1, len(pos)):
        if pos[i] - pos[last_idx] >= dist:
            count += 1
            last_idx = i
            
    return count

n, c = map(int, input().split())
pos = sorted([int(input()) for _ in range(n)])
print(upper_bound(c) - 1)
