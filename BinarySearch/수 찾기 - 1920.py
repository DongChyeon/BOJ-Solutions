n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
choose = list(map(int, input().split()))

for x in choose:
    if x in numbers:
        print(1)
    else:
        print(0)