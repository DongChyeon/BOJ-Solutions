def binary_search(data, target):
    start, end = 0, len(data) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        
    return 0

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
target_cards = list(map(int, input().split()))

for card in target_cards:
    print(binary_search(cards, card), end = ' ')
