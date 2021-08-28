e, s, m = map(int, input().split())
year = 1
E, S, M = 1, 1, 1

while E != e or S != s or M != m:
    E, S, M = E + 1, S + 1, M + 1
    
    # 해당 범위가 넘어가면 1로 갱신
    if E > 15:
        E = 1
    if S > 28:
        S = 1
    if M > 19:
        M = 1
    
    year += 1
    
print(year)
