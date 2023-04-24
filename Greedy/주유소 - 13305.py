n = int(input())
length = list(map(int, input().split()))
stations = list(map(int, input().split()))
stations = stations[:-1]

answer = 0

i = 0
while i < len(stations):
    answer += stations[i] * length[i]
    
    last_station = stations[i]
    while i + 1 < len(stations) and last_station < stations[i + 1]:
        i += 1
        answer += last_station * length[i]
    i += 1

print(answer)
