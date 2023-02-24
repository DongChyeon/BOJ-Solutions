def divideable_size(size, data):
    count = 1
    temp_size = 0
    
    for i in range(len(data)):
        temp_size += data[i]
        if temp_size > size:
            count += 1
            temp_size = data[i]
            
    return count

# 찾고자 하는 값 이상이 처음 나타나는 위치를 구함
def binary_search(target, array):
    start, end = max(array), sum(array)
    
    while start <= end:
        mid = (start + end) // 2
        
        if divideable_size(mid, array) > target:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

n, m = map(int, input().split())
data = list(map(int, input().split()))
print(binary_search(m, data))
