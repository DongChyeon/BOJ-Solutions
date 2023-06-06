import math

def is_prime_number(num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
            
    return True
    
def dfs(level, number):
    if level == n:
        print(number)
        return
    
    for num in range(1, 10):
        new_number = number + str(num)
        if is_prime_number(int(new_number)):
            dfs(level + 1, new_number)
    
n = int(input())
dfs(0, '')
