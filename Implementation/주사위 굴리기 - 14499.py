from collections import deque

'''
dice_y[1]과 dice_x[1]은 같음 - 주사위의 윗면
dice_y[3] - 주사위의 바닥면

주사위를 동쪽으로 굴릴 때 : dice_x.rotate(1) / dice_x[0], dice_y[3] = dice_y[3], dice_x[0] / dice_x[1] = dice_y[1]
주사위를 서쪽으로 굴릴 때 : dice_x.rotate(-1) / dice_x[2], dice_y[3] = dice_y[3], dice_x[2] / dice_x[1] = dice_y[1]
주사위를 북쪽으로 굴릴 떄 : dice_y.rotate(-1)
주사위를 남쪽으로 굴릴 때 : dice_y.rotate(1)
'''

dice_y = deque([0, 0, 0, 0])
dice_x = deque([0, 0, 0])

n, m, y, x, k = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

for command in commands:
    if command == 1:
        nx, ny = x + 1, y
        if nx > m - 1:
            continue
        x, y = nx, ny
        dice_x.rotate(1)
        dice_x[0], dice_y[3] = dice_y[3], dice_x[0]
        dice_y[1] = dice_x[1]
        
        if field[y][x] == 0:
            field[y][x] = dice_y[3]
        else:
            dice_y[3] = field[y][x]
            field[y][x] = 0
        print(dice_x[1])
            
    elif command == 2:
        nx, ny = x - 1, y
        if nx < 0:
            continue
        x, y = nx, ny
        dice_x.rotate(-1)
        dice_x[2], dice_y[3] = dice_y[3], dice_x[2]
        dice_y[1] = dice_x[1]
        
        if field[y][x] == 0:
            field[y][x] = dice_y[3]
        else:
            dice_y[3] = field[y][x]
            field[y][x] = 0
        print(dice_x[1])
            
    elif command == 3:
        nx, ny = x, y - 1
        if ny < 0:
            continue
        x, y = nx, ny
        dice_y.rotate(-1)
        dice_x[1] = dice_y[1]
        
        if field[y][x] == 0:
            field[y][x] = dice_y[3]
        else:
            dice_y[3] = field[y][x]
            field[y][x] = 0
        print(dice_x[1])
            
    elif command == 4:
        nx, ny = x, y + 1
        if ny > n - 1:
            continue
        x, y = nx, ny
        dice_y.rotate(1)
        dice_x[1] = dice_y[1]
        
        if field[y][x] == 0:
            field[y][x] = dice_y[3]
        else:
            dice_y[3] = field[y][x]
            field[y][x] = 0
        print(dice_x[1])
