# size만큼의 이미지가 같은 색인지 판별
def check(x, y, size):
    color = image[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if image[i][j] != color:
                return False
                
    return True

# 이미지가 같은 색이 아니라면 4분할    
def divide(x, y, size):
    global answer
    
    if check(x, y, size):
        answer += image[y][x]
    else:
        size = size // 2
        answer += '('
        for i in range(2):
            for j in range(2):
                divide(x + size * j, y + size * i, size)
        answer += ')'

n = int(input())
image = [list(input()) for _ in range(n)]
answer = ''
divide(0, 0, n)

print(answer)
