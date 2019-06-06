b=int(input())
a=input().split()
c=[x for n, x in enumerate(a) if x in a[:n]]
c=list(dict.fromkeys(c))
c.sort()
for i in c:
	print(i,end=" ")
