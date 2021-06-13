n = int(input())
number_of_doom = '666'
num = 666

while n:
    if number_of_doom in str(num):
        n -= 1
    if n == 0:
        print(num)
        break
    num += 1
