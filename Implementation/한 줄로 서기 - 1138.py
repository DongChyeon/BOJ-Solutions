n = int(input())
people = []
data = list(map(int, input().split()))

for i in range(len(data) - 1, -1, -1):
    count = data[i]
    
    idx = 0
    while True:
        if count == 0 or idx > len(people):
            people.insert(idx, i + 1)
            break
        if people[idx] > i + 1:
            count -= 1
        idx += 1
    
for x in people:
    print(x, end=' ')
