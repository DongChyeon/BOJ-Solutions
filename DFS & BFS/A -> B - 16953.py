def dfs(num, count):
    global answer
    
    if num == b:
        answer = min(answer, count)
    # num이 목표값 b보다 높아질 경우 탐색 종료    
    if num > b:
        return
    # 2를 곱하는 연산, 1을 수의 오른쪽에 추가하는 연산
    dfs(num * 2, count + 1)
    dfs(num * 10 + 1, count + 1)

a, b = map(int, input().split())
answer = int(10e9)
dfs(a, 1)

if answer == int(10e9):
    print(-1)
else:
    print(answer)
