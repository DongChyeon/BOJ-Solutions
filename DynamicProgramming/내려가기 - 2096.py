import copy

n = int(input())

up1 = list(map(int, input().split()))
up2 = copy.deepcopy(up1)

for _ in range(n - 1):
    down1 = list(map(int, input().split()))
    down2 = copy.deepcopy(down1)
    
    # 최댓값 구하기
    down1[0] += max(up1[0], up1[1])
    down1[1] += max(up1)
    down1[2] += max(up1[1], up1[2])
    
    # 최솟값 구하기
    down2[0] += min(up2[0], up2[1])
    down2[1] += min(up2)
    down2[2] += min(up2[1], up2[2])
    
    up1 = down1
    up2 = down2
    
print(max(up1), end=' ')
print(min(up2))
