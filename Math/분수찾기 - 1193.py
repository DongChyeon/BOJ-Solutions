x = int(input())

c = 1
count = 1
direction = 0 # 아래에서 위는 0, 위에서 아래는 1

while True:
    if x - c <= 0:
        remain = x
        break
    x -= c
    c += 1
    count += 1
    if direction == 0:
        direction = 1
    else:
        direction = 0

a = count # 분자
b = 1 # 분모

if a == 1:
    print("1/1")
else:
    for i in range(remain - 1):
        a -= 1
        b += 1
    if direction == 0:
        print(str(a) + '/' + str(b))
    else:
        print(str(b) + '/' + str(a))
