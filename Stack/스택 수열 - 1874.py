from collections import deque

n = int(input())
sequence = []
stack = []
answer = []

for _ in range(n):
    sequence.append(int(input()))

# 수열의 위치를 가리키는 변수
idx = 0
# 스택에 다음으로 push할 수
num = 1
while True:
    # 입력된 수열의 범위나 push할 수 의 범위가 벗어난 경우 종료
    if idx == n or num > n + 1:
        break
    
    if stack and stack[-1] == sequence[idx]:
        stack.pop()
        idx += 1
        answer.append('-')
    else:
        stack.append(num)
        num += 1
        answer.append('+')

# 스택에 남아 있는 게 있을 경우 만들기 불가능한 수열        
if stack:
    print('NO')
else:
    for x in answer:
        print(x)
