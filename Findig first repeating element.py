b=int(input())
a=input().split()
for i in a:
	c=a.count(i)
	if c>1:
		print(i)
		break
	elif (a.index(i)==len(a)-1):
		print("unique")
