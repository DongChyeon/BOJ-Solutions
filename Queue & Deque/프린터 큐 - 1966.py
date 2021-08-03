from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    prev_len = len(queue)
    
    for i in range(len(queue)):
        queue[i] = (queue[i], i)
        
    popped = -1    
    while popped != m:
        target = queue[0]
        
        # 큐 안에 중요도가 더 높은 문서가 있을 경우
        max_flag = True
        for x in queue:
            if target[0] < x[0]:
                max_flag = False
                break
        
        # 첫번째 문서를 큐의 맨 뒤쪽으로 보냄    
        if not max_flag:
            queue.rotate(-1)
        # 해당 문서가 가장 중요도가 높을 경우 출력
        else:
            popped = queue.popleft()[1]
            
    # m번째 문서가 몇 번째로 인쇄되는지 출력력    
    print(prev_len - len(queue))
