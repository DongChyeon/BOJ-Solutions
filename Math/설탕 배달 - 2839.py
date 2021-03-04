import math

n = int(input())

if n == 0:
    print(-1)
elif n % 5 == 0:
    print(n // 5)
else:
    a = math.floor(n / 5) # 5kg 짜리의 개수

    while True:
        if (n - (5 * a)) % 3 == 0:
            print(a + (n - (5 * a)) // 3)
            break
        # 5kg 짜리로 못담을 때
        if a == 0:
            if n % 3 == 0:
                print(n // 3)
            else:
                print(-1)
            break
        a -= 1