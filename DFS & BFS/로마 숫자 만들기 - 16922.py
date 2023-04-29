def dfs(start, count, total):
    global answer
    
    numbers = [1, 5, 10, 50]
    
    if count == n:
        if total not in answer:
            answer.append(total)
        return
    for i in range(start, 4):
        dfs(i, count + 1, total + numbers[i])
        
n = int(input())
answer = []

dfs(0, 0, 0)
print(len(answer))
