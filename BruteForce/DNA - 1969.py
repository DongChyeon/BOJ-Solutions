n, m = map(int, input().split())
dna = [input() for _ in range(n)]
answer = ''

for i in range(m):
    # 0 : A / 1 : C / 2 : G / 3 : T
    dna_cnt = [0, 0, 0, 0]
    for j in range(n):
        cur_dna = dna[j]
        if cur_dna[i] == 'A':
            dna_cnt[0] += 1
        elif cur_dna[i] == 'C':
            dna_cnt[1] += 1
        elif cur_dna[i] == 'G':
            dna_cnt[2] += 1
        elif cur_dna[i] == 'T':
            dna_cnt[3] += 1
            
    if max(dna_cnt) == dna_cnt[0]:
        answer += 'A'
    elif max(dna_cnt) == dna_cnt[1]:
        answer += 'C'
    elif max(dna_cnt) == dna_cnt[2]:
        answer += 'G'
    elif max(dna_cnt) == dna_cnt[3]:
        answer += 'T'
        
hamming_distance = 0
for i in range(n):
    for j in range(m):
        if answer[j] != dna[i][j]:
            hamming_distance += 1
        
print("%s\n%d" % (answer, hamming_distance))
