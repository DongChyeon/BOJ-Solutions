def nqueen(current):
    # current는 현재 몇 개의 퀸이 배치되었는지 의미하는 변수
    global answer
    
    if current == n:
        answer += 1
        return
    
    for i in range(n):
        cnt = 1
        for j in range(current):
            # 이미 배치된 퀸들을 통해 놓을 수 있는지 여부 판별
            # 같은 열, 대각선상에 존재 불가
            # 행 번호 차이 = 열 번호 차이라면 같은 대각선상에 존재하는 것
            if board[j] == i or abs(current - j) == abs(i - board[j]):
                cnt = 0
                break
        if cnt > 0:
            board[current] = i
            nqueen(current + 1)

n = int(input())
board = [-1] * n
answer = 0

nqueen(0)

print(answer)
