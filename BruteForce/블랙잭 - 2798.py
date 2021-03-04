from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

comb = combinations(cards, 3)

min_difference = 300000
# m 보다 크지 않은 최대한 가까운 카드의 합을 찾아냄
for x in comb:
    if m - sum(x) >= 0:
        min_difference = min(min_difference, m - sum(x))

print(m - min_difference)