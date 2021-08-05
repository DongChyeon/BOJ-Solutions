expr = input()
parts = expr.split('-')
# +부분을 모두 먼저 더해서 나중에 빼줌
for i in range(len(parts)):
    plus_parts = list(map(int, parts[i].split('+')))
    total = plus_parts[0]
    for j in range(1, len(plus_parts)):
        total += plus_parts[j]
    parts[i] = total

answer = parts[0]
for i in range(1, len(parts)):
    answer -= parts[i]

print(answer)
