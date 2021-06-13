n = int(input())
answer = int(1e6)

for num in range(1, n + 1):
    total = num
    for x in str(num):
        total += int(x)
    if total == n and num < answer:
        answer = num
  
if answer == int(1e6):
    print(0)
else:
    print(answer)
