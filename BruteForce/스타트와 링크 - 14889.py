# 사전식 순서의 순열을 만들어냄 (현재 순열보다 큰 순열을 만들기 때문에 중복 제거)
def next_permutation(arr):
    # 꼭대기 값 앞자리를 찾아냄 (뒤에서 시작했을 때 오름차순이 끝나는 지점)
    # 그러한 꼭대기 값이 발견되지 않을 경우 현재 순열이 마지막 순열
    for i in reversed(range(len(arr) - 1)):
        if arr[i] < arr[i + 1]:
            break
    else:
        return False

    # arr[i] > arr[j] 일 때 가장 큰 j를 찾아냄 (꼭대기값 앞자리와 교환할 값을 찾음)
    j = next(j for j in reversed(range(i + 1, len(arr))) if arr[i] < arr[j])

    # 두 값 교환
    arr[i], arr[j] = arr[j], arr[i]

    # 꼭대기부터 뒤까지 오름차순으로 정렬
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return True
        
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    
answer = int(10e9)

# 0은 스타트팀, 1은 링크팀으로 가정해서 순열 생성
pool = [0] * (n // 2) + [1] * (n // 2)
while True:
    if not next_permutation(pool):
        break
    
    # 0은 스타트팀, 1은 링크팀
    start, link = [], []
    for i in range(len(pool)):
        if pool[i] == 0:
            start.append(i)
        else:
            link.append(i)

    start_total, link_total = 0, 0
    
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            if i == j:
                continue
            
            # 각 팀에서 두명씩 뽑아서 점수 계산
            start_total += data[start[i]][start[j]] + data[start[j]][start[i]]
            link_total += data[link[i]][link[j]] + data[link[j]][link[i]]
            
    # 두 팀의 점수차가 가장 적을 때가 답
    answer = min(answer, abs(start_total - link_total))
    
print(answer)
