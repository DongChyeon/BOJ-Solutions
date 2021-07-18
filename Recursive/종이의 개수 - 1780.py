# size만큼의 종이가 같은 색이지 판별
def check(x, y, size):
    color = paper[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != color:
                return False
                
    return True
    
# 색이 같지 않을 경우 3분할
def divide(x, y, num):
    if check(x, y, num):
        answer[paper[y][x] + 1] += 1
    else:
        size = num // 3
        for i in range(3):
            for j in range(3):
                divide(x + size * i, y + size * j, size)
                
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
# -1로 채워진 종이의 개수, 0으로 채워진 종이의 개수, 1로 채워진 종의 개수
answer = [0, 0, 0]
divide(0, 0, n)

for x in answer:
    print(x)
