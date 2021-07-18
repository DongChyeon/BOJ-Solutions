def combinations(at, depth):
    # 6개를 고르면 출력
    if depth == 6:
        for x in comb:
            print(x, end=' ')
        print()
        return
    
    for i in range(at, n):
        comb[depth] = pool[i]
        # 이전에 탐색한 곳을 탐색하지 않음
        combinations(i + 1, depth + 1)

while True:
    data = list(map(int, input().split()))
    n = data[0]
    if n == 0:
        break
    pool = data[1:]
    comb = [0 for _ in range(6)]
    
    combinations(0, 0)
    print()
