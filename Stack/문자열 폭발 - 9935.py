string = input()
explosion = input()

stack = []
for i in range(len(string)):
    stack.append(string[i])
    # 폭발 문자열보다 길이가 길어지면 폭발 가능성 검사
    if len(stack) >= len(explosion):
        explosion_flag = True
        for i in range(-len(explosion), 0):
            if stack[i] != explosion[i]:
                explosion_flag = False
        # 문자열 폭발
        if explosion_flag:
            for _ in range(len(explosion)):
                stack.pop()
                
if stack:
    print(''.join(x for x in stack))
else:
    print('FRULA')
