n = int(input())
remain = n - 1
border = 1
result = 1

if remain == 0 :
    print(result)
else:
    while remain > 0:
        # 바깥쪽으로 갈수록 테두리 칸의 개수가 6개씩 늘어남
        remain -= border * 6
        result += 1
        border += 1
    print(result)
