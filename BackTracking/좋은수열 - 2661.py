def dfs(level, current):
    if level == n:
        print(current)
        exit(0)
    
    for i in range(1, 4):
        sequence = current + str(i)
        if promising(sequence):
            dfs(level + 1, sequence)
    
def promising(sequence):
    if len(sequence) < 2:
        return True
        
    size = len(sequence)
    mid = size // 2
    for i in range(1, mid + 1):
        if sequence[-(2 * i):-i] == sequence[-i:]:
            return False
            
    return True

n = int(input())
dfs(0, '')
