from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
answer = 0

# data로 만들 수 있는 모든 순열을 비교해 최댓값을 구함
for x in list(permutations(data)):
    total = 0
    for i in range(n - 1):
        total += abs(x[i] - x[i + 1])        
    answer = max(answer, total)
    
print(answer)
