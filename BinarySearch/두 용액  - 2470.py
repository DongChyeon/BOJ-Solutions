n = int(input())
data = sorted(list(map(int, input().split())))

# 투 포인터 이용
left, right = 0, len(data) - 1
min_val = abs(data[left] + data[right])
answer = (data[left], data[right])

while left < right:
    if abs(data[left] + data[right]) < min_val:
        min_val = abs(data[left] + data[right])
        answer = (data[left], data[right])
        # 0을 발견하면 탐색 종료
        if min_val == 0:
            break
    
    if data[left] + data[right] < 0:
        left += 1
    elif data[left] + data[right] > 0:
        right -= 1
        
print(answer[0], answer[1])
