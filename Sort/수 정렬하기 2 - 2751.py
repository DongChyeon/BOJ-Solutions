n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

for num in sorted(numbers):
    print(num)