s = input()
str_list = []

temp, idx = '' , 0
while True:
    if idx > len(s) - 1:
        break
    
    if s[idx] == '<':
        str_list.append(temp[::-1])
        temp = s[idx]
        while True:
            idx += 1
            temp += s[idx]
            if s[idx] == '>':
                str_list.append(temp)
                temp = ''
                break
    elif s[idx] == ' ':
        str_list.append(temp[::-1])
        str_list.append(' ')
        temp = ''
    else:
        temp += s[idx]
        
    idx += 1
str_list.append(temp[::-1])

print(''.join(str_list))
