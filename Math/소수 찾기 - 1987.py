import math

def is_prime_number(n):
    count = 0
    
    if n == 1:
        return False
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False

n = int(input())
numbers = map(int, input().split())
result = 0

for num in numbers:
    if is_prime_number(num):
        result += 1

print(result)