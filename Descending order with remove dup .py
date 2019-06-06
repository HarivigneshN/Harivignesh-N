b=int(input())
a=input().split()
a=list(dict.fromkeys(a))
a=sorted(a, reverse=True)
for i in a:
	print(i,end="")
