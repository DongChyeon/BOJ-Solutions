from collections import deque

k = int(input())
stack = deque([])

for _ in range(k):
    num = int(input())
    # 0일 경우 stack의 top을 pop
    if num == 0:
        stack.popleft()
    else:
        stack.insert(0, num)

print(sum(stack))