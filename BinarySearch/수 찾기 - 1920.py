n = int(input())
a = sorted([int(i) for i in input().split()])

m = int(input())
numbers = [int(i) for i in input().split()]

# 이분 탐색 이용
for num in numbers:
    start, end = 0, len(a) - 1
    is_exist = False
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == num:
            is_exist = True
            break
        elif a[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    
    if is_exist:
        print(1)
    else:
        print(0)
