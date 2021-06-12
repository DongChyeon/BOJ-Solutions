import sys

input = sys.stdin.readline

while True:
    stack = []
    flag = True
    sentence = input().rstrip()
    
    if sentence == '.':
        break
    for char in sentence:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False

        elif char == '[':
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
            
    if not stack and flag:
        print('yes')
    else:
        print('no')
