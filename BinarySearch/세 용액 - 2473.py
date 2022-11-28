n = int(input())
data = sorted(list(map(int, input().split())))

min_val = abs(data[0] + data[1] + data[2])
answer = (data[0], data[1], data[2])

for left in range(len(data) - 2):
    mid, right = left + 1, len(data) - 1
    while mid < right:
        total = data[left] + data[mid] + data[right]
        
        if abs(total) < min_val:
            min_val = abs(total)
            answer = (data[left], data[mid], data[right])
            # 0을 발견하면 탐색 종료
            if min_val == 0:
                break
            
        if total < 0:
            mid += 1
        else:
            right -=1
    
print(answer[0], answer[1], answer[2])
