a=input().split()
b=[]
c=int(a[1])
for i in a:
	for j in i:
		b.append(j)
d=b[c:len(b)-1]
for i in d:
	print(i,end='')
