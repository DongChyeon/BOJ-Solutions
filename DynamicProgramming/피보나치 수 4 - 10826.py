n = int(input())

if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    # n - 1번째 피보나치 수와 n번째 피보나치 수로 계속 갱신
    fibonacci = [1, 1]
    for _ in range(n - 2):
        fibonacci[0], fibonacci[1] = fibonacci[1], fibonacci[0] + fibonacci[1]
    
    print(fibonacci[1])
