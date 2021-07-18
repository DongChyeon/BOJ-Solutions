import copy

# 행렬의 곱셈
def matrix_multiply(a, b):
    c = [[0] * len(a) for _ in range(len(b[0]))]
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            total = 0
            for k in range(len(a[0])):
                total += a[i][k] * b[k][j]
            # 수가 너무 커질 수 있으니 1000으로 나눈 나머지로 처리
            c[i][j] = total % 1000
            
    return c
    
# A^n/2 * A^n/2 = A^n
def solve(matrix, n):
    # n이 1이 될 때까지 반으로 계속 분할한 다음 합침
    if n > 1:
        matrix = solve(matrix, n // 2)
        matrix = matrix_multiply(matrix, matrix)
        
        # n이 홀수일 경우 (2로 나누면서 버려지는 1을 고려)
        if n & 1:
            matrix = matrix_multiply(matrix, matrix_b)
            
    return matrix

n, b = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
matrix_b = copy.deepcopy(matrix_a)
matrix_a = solve(matrix_a, b)

for row in matrix_a:
    for col in row:
        print(col % 1000, end=' ')
    print()
