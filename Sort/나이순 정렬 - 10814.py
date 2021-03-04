n = int(input())
persons = []

for _ in range(n):
    age, person = input().split()
    persons.append((int(age), person))

# 첫 번째 값(나이)를 기준으로 정렬
for person in sorted(persons, key = lambda x : x[0]):
    print(person[0], person[1])