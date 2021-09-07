import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n - 1, -1, -1):
    # 스택의 top이 data[i] 보다 커질 때까지 pop
    while stack and stack[-1] <= data[i]:
        stack.pop()
    # 스택이 비어있게 되면 오큰수가 없으므로 -1
    if not stack:
        answer[i] = -1
    # i 번째 수의 오큰수는 스택의 top
    else:
        answer[i] = stack[-1]
        
    # 다시 스택에 넣어줌
    stack.append(data[i])
    
for x in answer:
    print(x, end=' ')
