from collections import Counter

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))
    
# 산술평균 출력    
print(round(sum(data) / n))

# 중앙값 출력
print(sorted(data)[n - (n // 2) - 1])

# 최빈값 출력
counter = Counter(data).most_common()
max_val = counter[0][1]

temp = []
for x in counter:
    if x[1] == max_val:
        temp.append(x[0])
    else:
        break

# 최빈값이 여러 개일 경우 두 번째로 작은 값 출력
if len(temp) == 1:
    print(temp[0])
else:
    print(sorted(temp)[1])

# 범위 출력
print(max(data) - min(data))
