b=int(input())
a=input().split()
d=[]
for i in range (0,len(a)):
	c=a[i]
	if (i==int(c)):
		d.append(i)
d=sorted(d)
for i in d:
	print(i,end=" ")
