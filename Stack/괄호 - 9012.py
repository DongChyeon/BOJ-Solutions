from collections import deque

# 올바른 괄호가 맞는지 판별
def is_vps(ps):
    stack = deque([])
    for ch in ps:
        if ch == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.popleft()

    if not stack:
        return True
    else:
        return False

n = int(input())

for _ in range(n):
    ps = input()
    if is_vps(ps):
        print("YES")
    else:
        print("NO")