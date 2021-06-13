# 연산자들간의 우선순위
def priority(oper):
    if oper == '*' or oper == '/':
        return 2
    elif oper == '+' or oper == '-':
        return 1
    else:
        return 0

exp = input()
operator = []

for ch in exp:
    if ch == '(':
        operator.append(ch)
    elif ch == ')':
        # 왼쪽 괄호가 나올때까지 스택에서 꺼내서 출력
        while True:
            temp = operator.pop()
            if temp == '(':
                break
            print(temp, end='')
    elif ch == '+' or ch == '-' or ch == '*' or ch == '/':
        # 스택의 top에 있는 연산자의 우선순위가 더 높을 경우 출력
        while operator and priority(operator[-1]) >= priority(ch):
            print(operator.pop(), end='')
        operator.append(ch)
    else:
        print(ch, end='')
        
while operator:
    print(operator.pop(), end='')
