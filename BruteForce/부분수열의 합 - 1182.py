from itertools import combinations

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

# 부분수열의 원소들을 구하고 원소들의 합이 s일 경우 개수 증가
for i in range(1, len(numbers) + 1):
    comb = list(combinations(numbers, i))
    for x in comb:
        if sum(x) == s:
            answer += 1
            
print(answer)
