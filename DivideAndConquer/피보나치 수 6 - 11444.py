# 2 x 2 행렬 제곱 함수
def matrix_multiply(a, b):
    temp = [[0, 0], [0, 0]]

    temp[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000007
    temp[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000007
    temp[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000007
    temp[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000007
    
    return temp

# A^n/2 * A*n/2 = A^n    
def solve(matrix_a, n):
    # n이 1이 될 때까지 반으로 계속 분할한 다음 합침
    if n > 1:
        matrix_a = solve(matrix_a, n // 2)
        matrix_a = matrix_multiply(matrix_a, matrix_a)
        
        # n이 홀수일 경우 (2로 나누면서 버려지는 1을 고려)
        if n & 1:
            matrix_b = [[1, 1], [1, 0]]
            matrix_a = matrix_multiply(matrix_a, matrix_b)
            
    return matrix_a

n = int(input())
# [[Fn+1, Fn], [Fn, Fn-1]]
matrix = [[1, 1], [1, 0]]
matrix = solve(matrix, n)
print(matrix[0][1])
