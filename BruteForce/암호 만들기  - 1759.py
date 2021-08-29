from itertools import combinations

l, c = map(int, input().split())
alphabets = list(input().split())
# 알파벳들 중에서 l개를 고르는 조합을 모두 구함
pool = list(combinations(alphabets, l))
answer = []

for x in pool:
    # 모음의 개수를 구함
    count = 0
    
    if 'a' in x:
        count += 1
    if 'e' in x:
        count += 1
    if 'i' in x:
        count += 1
    if 'o' in x:
        count += 1
    if 'u' in x:
        count += 1
    
    # 모음이 1개 이상 자음이 2개 이상 있을시 추가   
    if count >= 1 and len(x) - count >= 2:
        answer.append(''.join(sorted(x)))
 
# 사전식으로 정렬해서 출력    
for x in sorted(answer):
    print(x)
