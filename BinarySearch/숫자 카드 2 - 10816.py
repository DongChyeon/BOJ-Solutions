# 찾고자 하는 값 이상이 처음 나타나는 위치를 구함
def lower_bound(array, target):
    start, end = 0, len(array)
    
    while start < end:
        mid = (start + end) // 2
        
        if target <= array[mid]:
            end = mid
        else:
            start = mid + 1
        
    return start

# 찾고자 하는 값보다 큰 값이 처음 나타나는 위치를 구함
def upper_bound(array, target):
    start, end = 0, len(array)
    
    while start < end:
        mid = (start + end) // 2
        
        if target < array[mid]:
            end = mid
        else:
            start = mid + 1
            
    return start
    
n = int(input())
my_cards = sorted(list(map(int, input().split())))
m = int(input())
cards = list(map(int, input().split()))

for card in cards:
    print(upper_bound(my_cards, card) - lower_bound(my_cards, card), end=' ') 
