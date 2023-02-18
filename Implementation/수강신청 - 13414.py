import sys

input = sys.stdin.readline

k, l = map(int, input().split())
queue = dict()
for i in range(l):
    student = input().rstrip('\n')
    queue[student] = i

queue = list(sorted(queue.items(), key = lambda x: x[1]))

idx = 0
while idx < len(queue) and idx < k:
    print(queue[idx][0])
    idx += 1
