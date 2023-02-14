from collections import deque

gears = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())
for _ in range(k):
    number, direction = map(int, input().split())
    
    '''
    맞닿은 곳이 서로 다른 극인지 판별 / gear1[2]와 gear2[6]은 맞닿은 상태
    rotatable[0] = 1번 톱니바퀴 - 2번 톱니바퀴
    rotatable[1] = 2번 톱니바퀴 - 3번 톱니바퀴
    rotatable[2] = 3번 톱니바퀴 - 4번 톱니바퀴
    '''
    
    rotatable = [False] * 3
    for i in range(3):
        if gears[i][2] != gears[i + 1][6]:
            rotatable[i] = True
    
    commands = [0] * 4
    commands[number - 1] = direction
    
    if number > 1:
        for i in range(number - 2, -1, -1):
            if rotatable[i]:
                commands[i] = -commands[i + 1]
            else:
                break
        
    if number < 4:
        for i in range(number - 1, 3):
            if rotatable[i]:
                commands[i + 1] = -commands[i]
            else:
                break
        
    for c in range(len(commands)):
        gears[c].rotate(commands[c])
        
answer = 0
for i in range(len(gears)):
    if gears[i][0]:
        answer += 2 ** i
    
print(answer)
