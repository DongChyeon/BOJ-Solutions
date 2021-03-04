n = int(input())
words = []

for _ in range(n):
    words.append(input())
words = list(set(words))
# 단어의 길이를 기준으로 오름차순, 길이가 같다면 단어 기준으로 오름차순 정렬
words.sort(key = lambda x : (len(x), x))

for word in words:
    print(word)