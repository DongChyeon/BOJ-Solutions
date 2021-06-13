n=int(input())
data=[]
big=[0 for x in range(n)]

for i in range(n):
	data.append(input().split())
	
for i in range(len(data)):
	for j in range(len(data)):
		if i!=j and data[i][0]<data[j][0] and data[i][1]<data[j][1]:
			big[i]+=1
			
for x in big:
	print(x+1, end=' ')
