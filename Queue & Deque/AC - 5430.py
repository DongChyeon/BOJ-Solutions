import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    # 뒤집기 여부를 나타내는 변수
    reverse_flag = False
    # 에러 여부를 나타내는 변수
    error_flag = False
    oper = input()
    n = int(input())
    arr = list(input().strip('[]\n').split(','))
    
    if n == 0:
        queue = deque()
    else:
        queue = deque(arr)
    
    for x in oper:
        if x == 'R':
            if reverse_flag:
                reverse_flag = False
            else:
                reverse_flag = True
        elif x == 'D':
            # 큐가 비어있으면 에러 출력
            if not queue:
                print('error')
                error_flag = True
                break
            if reverse_flag:
                queue.pop()
            else:
                queue.popleft()
    # 에러가 나지 않았다면 queue의 내용 출력
    if not error_flag:            
        if reverse_flag:
            print('[', end='')
            if queue:
                for i in range(len(queue) - 1, 0, -1):
                    print(queue[i], end=',')
                print(queue[0], end='')
            print(']')
        else:
            print('[', end='')
            if queue:
                for i in range(len(queue) - 1):
                    print(queue[i], end=',')
                print(queue[-1], end='')
            print(']')
