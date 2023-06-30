def dfs():    
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    last_num = 0
    for i in range(len(numbers)):
        if not visited[i]:
            # 이전 수열과 추가할 수가 같을 시 중복 처리
            if last_num == numbers[i]:
                continue
            visited[i] = True
            sequence.append(numbers[i])
            last_num = numbers[i]
            dfs()
            sequence.pop()
            visited[i] = False

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * (len(numbers))
sequence = []
dfs()
