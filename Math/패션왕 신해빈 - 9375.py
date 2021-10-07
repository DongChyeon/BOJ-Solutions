from itertools import combinations

t = int(input())

for _ in range(t):
    # 각 의상의 종류가 몇 개 있는지 closet 딕셔너리를 초기화
    closet = dict()
    n = int(input())
    for _ in range(n):
        costume, kind = input().split()
        if kind not in closet.keys():
            closet[kind] = 1
        else:
            closet[kind] += 1

    answer = 1
    for v in closet.values():
        # 각 종류별 옷을 입는 경우 (안 입는 경우 포함)
        answer *= v + 1
    # 옷을 아무것도 안 입는 경우는 빼줌
    answer -= 1

    print(answer)
