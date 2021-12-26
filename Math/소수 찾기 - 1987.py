import math

# 에라토스테네스의 체 이용
m, n = map(int, input().split())
if n >= 2:
    a = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        a[i] = i
    
    # 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지움
    for i in range(2, int(math.sqrt(n)) + 1):
        if a[i] == 0:
            continue
        for j in range(2 * i, n + 1, i):
            a[j] = 0
    # 2는 소수이므로 제외
    a[2] = 2        
        
    for i in range(m, n + 1):
        if a[i] != 0:
            print(i)
