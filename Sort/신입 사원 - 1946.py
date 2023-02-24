t = int(input())

for _ in range(t):
    n = int(input())
    
    people = []
    for _ in range(n):
        a, b = map(int, input().split())
        people.append((a, b))
        
    people.sort(key = lambda x : x[0])
    
    answer = 1
    
    # 자신보다 서류 순위가 높은 사람들보다 면접 순위가 높아야 함함
    min_rank = people[0][1]
    for i in range(1, n):
        if people[i][1] < min_rank:
            answer += 1
            min_rank = people[i][1]
        
    print(answer)
