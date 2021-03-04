a, b, c = map(int, (input().split()))

if b >= c:
    print(-1)
else:
    if a == 0:
        print(1)
    else:
        print(a // (c - b) + 1)
