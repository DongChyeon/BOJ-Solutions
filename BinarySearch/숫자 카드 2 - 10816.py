import sys

# 찾는 값의 가장 작은 인덱스를 반환함
def binary_search(array, target):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            while mid > 0:
                if array[mid - 1] == target:
                    mid -= 1
                else:
                    break
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
my_cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

card_dict = {}

for card in my_cards:
    if card not in card_dict:
        idx = binary_search(cards, card)
        # 몇 개의 같은 수가 있는지 알아냄
        if idx is not None:
            count = 0
            for i in range(idx, len(cards)):
                if cards[i] == card:
                    count += 1
                else:
                    break
        else:
            count = 0
        # 딕셔너리에 저장
        card_dict[card] = count

print(' '.join(str(card_dict[x]) for x in my_cards))