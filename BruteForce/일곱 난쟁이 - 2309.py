from itertools import combinations

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

# 난쟁이가 7명인 모든 조합을 구함    
comb = combinations(dwarfs, 7)

# 일곱 난쟁이들의 키가 100이면 출력
for x in comb:
    if sum(x) == 100:
        for dwarf in sorted(x):
            print(dwarf)
        break
