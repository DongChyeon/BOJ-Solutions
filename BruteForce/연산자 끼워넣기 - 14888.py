# 사전식 순열을 구함으로써 중복되는 순열을 없앰
def next_permutation(arr):
    for i in reversed(range(len(arr) - 1)):
        if arr[i] < arr[i + 1]:
            break
    else:
        return False
        
    j = next(j for j in reversed(range(i + 1, len(arr))) if arr[i] < arr[j])
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return True

n = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))
pool = []

# 1 : 덧셈 / 2 : 뺄셈 / 3 : 곱셈 / 4 : 나눗셈
for x in range(opers[0]):
    pool.append(1)
for x in range(opers[1]):
    pool.append(2)
for x in range(opers[2]):
    pool.append(3)
for x in range(opers[3]):
    pool.append(4)
    
max_val, min_val = -int(10e9), int(10e9)
pool.sort()

total = numbers[0]
for i in range(1, len(numbers)):
    oper = pool[i - 1]
    if oper == 1:
        total += numbers[i]
    elif oper == 2:
        total -= numbers[i]
    elif oper == 3:
        total *= numbers[i]
    elif oper == 4:
        # 음수를 양수로 나눌 때는 C++14의 기준을 따름
        if total < 0:
            temp = -total // numbers[i]
            total = -temp
        else:
            total //= numbers[i]
        
max_val = max(total, max_val)
min_val = min(total, min_val)

while True:
    if not next_permutation(pool):
        break
    
    total = numbers[0]
    for i in range(1, len(numbers)):
        oper = pool[i - 1]
        if oper == 1:
            total += numbers[i]
        elif oper == 2:
            total -= numbers[i]
        elif oper == 3:
            total *= numbers[i]
        elif oper == 4:
            # 음수를 양수로 나눌 때는 C++14의 기준을 따름
            if total < 0:
                temp = -total // numbers[i]
                total = -temp
            else:
                total //= numbers[i]
            
    max_val = max(total, max_val)
    min_val = min(total, min_val)

print(max_val)
print(min_val)
