n = int(input())
data = []
for _ in range(n):
    start, end = map(int, input().split())
    data.append((start, end))
# 회의가 일찍 끝나는 순서, 일찍 시작하는 순서로 정렬
data.sort(key = lambda x : (x[1], x[0]))

answer = 0
end_time = 0
# 이전 회의의 끝나는 시간과 이번 회의의 시작하는 시간이 크거나 같다면 갱신
for i in range(n):
    if data[i][0] >= end_time:
        answer += 1
        end_time = data[i][1]
        
print(answer)
