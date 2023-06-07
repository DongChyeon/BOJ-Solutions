from collections import deque

def bfs():
    queue = deque(answers)
    
    while queue:
        if len(answers) > n:
            print(answers[n])
            return
        
        number = queue.popleft()
        for i in range(10):
            new_number = number + str(i)
            if promising(new_number):
                answers.append(new_number)
                queue.append(new_number)
    
    print(-1)
    
def promising(number):
    if len(number) == 1:
        return True
    if number[-2] > number[-1]:
        return True
    return False

n = int(input())
answers = [str(i) for i in range(10)]
bfs()
