from itertools import combinations

n, m = map(int, input().split())
field = [list(map(int, input().split())) for x in range(n)]
chicken_house = []
house = []

answer = int(10e9)

for y in range(n):
    for x in range(n):
        if field[y][x] == 1:
            house.append((y, x))
        elif field[y][x] == 2:
            chicken_house.append((y, x))

# 치킨 집을 m개 고르는 경우의 수를 구함            
comb = combinations(chicken_house, m)

# 각각의 조합에 대한 치킨 거리를 구해봄
for ch in comb:
    total = 0
    
    # 각 집에서 가장 가까운 치킨집의 거리를 구함
    for h in house:
        min_dist = 100
        for x in ch:
            min_dist = min(min_dist, abs(x[0] - h[0]) + abs(x[1] - h[1]))
        total += min_dist
    
    # 최소 치킨 거리 갱신
    answer = min(answer, total)
    
print(answer)
