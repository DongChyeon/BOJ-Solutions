def hanoi(n, start, to, via):
    if n == 1:
        print(start, to)
    else:
        # 중간 기둥으로 n - 1개 옮겨야함
        hanoi(n - 1, start, via, to)
        print(start, to)
        # 중간 기둥에 있는 것을 다시 옮김
        hanoi(n - 1, via, to, start)

n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3, 2)