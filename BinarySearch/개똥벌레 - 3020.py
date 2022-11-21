# 찾고자 하는 값 이상이 처음 나타나는 위치를 구함
def lower_bound(array, target):
    start, end = 0, len(array)
    
    while start < end:
        mid = (start + end) // 2
        
        if target <= array[mid]:
            end = mid
        else:
            start = mid + 1
        
    return start

n, h = map(int, input().split())

tites, mites = [], []
for _ in range(n // 2):
    tites.append(int(input()))
    mites.append(int(input()))
tites.sort()
mites.sort()

obs_cnt = [0] * h

for i in range(len(obs_cnt)):
    # 해당 구간에 있는 종유석과 석순의 개수를 구함
    obs_cnt[i] = n // 2 - lower_bound(tites, i + 1) + n // 2 - lower_bound(mites, h - i)

print(min(obs_cnt), obs_cnt.count(min(obs_cnt)))
