n, m, b = map(int, input().split())
field = [[int(i) for i in input().split()] for _ in range(n)]
cost, height = int(10e9), 0

for h in range(257):
    # 쌓아야 할 블록과 제거해야 될 블록을 계산함
    build, remove = 0, 0
    for i in range(n):
        for j in range(m):
            if h > field[i][j]:
                build += h - field[i][j]
            else:
                remove += field[i][j] - h
    
    # 인벤토리에 있는 블록 + 제거해야 될 블록이 쌓아야 할 블록과 같거나 클 경우 소요시간 계산            
    if remove + b >= build:
        if cost >= remove * 2 + build:
            cost = remove * 2 + build
            height = h
                
print(cost, height)
