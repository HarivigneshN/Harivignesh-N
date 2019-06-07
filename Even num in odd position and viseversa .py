z=int(input())
a=input().split()
b=[]
for i in range (0,len(a)):
	c=int(a[i])
	if i>0:
		if i%2!=0 and c%2==0:
			print(c,end=" ")
		elif i%2==0 and c%2!=0:
			print(c,end=" ")
	elif c%2!=0:
		print(c,end=" ")
