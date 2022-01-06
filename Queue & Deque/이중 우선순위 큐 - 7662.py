import heapq
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    # 최대 힙, 최소 힙 생성
    max_heap, min_heap = [], []
    erased = [0] * 1000001
    k = int(input())
    for i in range(k):
        oper, num = input().split()
        if oper == 'I':
            heapq.heappush(max_heap, (-int(num), i))
            heapq.heappush(min_heap, (int(num), i))
        # 최댓값을 삭제하고 지운 목록에 추가
        elif int(num) == 1:
            while max_heap and erased[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                erased[heapq.heappop(max_heap)[1]] = 1
        # 최솟값을 삭제하고 지운 목록에 추가
        elif int(num) == -1:
            while min_heap and erased[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                erased[heapq.heappop(min_heap)[1]] = 1
    
    # 최대 힙과 최소 힙에서 지운 값들 제거    
    while max_heap and erased[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and erased[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    # 남아 있는 값들 중 가장 큰 값과 작은 값 출력            
    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
