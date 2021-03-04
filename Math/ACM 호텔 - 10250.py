t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        a, b = str(h), str(n // h)
    else:
        a, b = str(n % h), str(n // h + 1)
    if len(b) == 1:
        b = '0' + b
    print(a + b)