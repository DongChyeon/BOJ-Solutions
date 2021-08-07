def divide(x, y, size):
    # 방문 순서를 나타내는 변수
    global count
    
    # 사이즈가 1이 될 때까지 4분할
    if size > 1:
        size = size // 2
        
        # x, y가 위치한 사분면을 탐색
        if r <= y - 1 + size and c <= x - 1 + size: 
            divide(x, y, size)
        elif r <= y - 1+ size and c <= x - 1 + (size * 2):
            count += size * size
            divide(x + size, y, size)
        elif r <= y - 1 + (size * 2) and c <= x - 1 + size:
            count += (size * size) * 2
            divide(x, y + size, size)
        else:
            count += (size * size) * 3
            divide(x + size, y + size, size)
    else:
        # 해당 사분면에서의 방문 순서 표시
        count += (r - y) * 2 + (c - x)
        print(count)

n, r, c = map(int, input().split())
count = 0
divide(0, 0, 2**n)
