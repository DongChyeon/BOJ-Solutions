# 찾고자 하는 값보다 큰 값이 처음 나타나는 위치를 구함
def upper_bound(target):
    start, end = 0, sum(data) + 1
    
    while start < end:
        mid = (start + end) // 2
        
        if target > check(mid):
            end = mid
        else:
            start = mid + 1
            
    return start
    
# score를 최소 점수로 했을 때 몇 개의 구간이 만들어지는지 체크
def check(score):
    count = 0
    total = 0
    
    for i in range(len(data)):
        total += data[i]
        if total >= score:
            count += 1
            total = 0
            
    return count

n, k = map(int, input().split())
data = list(map(int, input().split()))
print(upper_bound(k) - 1)
