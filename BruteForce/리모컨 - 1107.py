from itertools import product

n = int(input())
m = int(input())

buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 고장난 버튼이 있는 경우
if m:
    broken = list(input().split())
    # 고장난 버튼 제거
    for x in broken:
        buttons.remove(x)

# 초기 채널에서 +, - 버튼만을 이용해 채널 변경을 하는 경우
answer1 = abs(100 - n)
# 채널을 입력한 다음 +, - 버튼을 이용해 채널 변경을 하는 경우
answer2 = int(10e9)
# 고장나지 않은 버튼들만으로 구성된 중복순열을 구함
if buttons:
    cases = list(map(''.join, product(buttons, repeat=len(str(n)))))
    # 자릿수 - 1 중 가장 큰 수
    if len(str(n)) > 1:
        cases.append(str(buttons[-1] * (len(str(n)) - 1)))
    # 자릿수 + 1 중 가장 큰 수
    temp = list(buttons[0] * (len(str(n)) + 1))
    if len(buttons) > 1 and temp[0] == '0':
        temp[0] = buttons[1]
    cases.append(''.join(temp))

    for x in cases:
        answer2 = min(answer2, (len(x) + abs(int(x) - n)))
    
print(min(answer1, answer2))
