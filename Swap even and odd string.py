a=input()
b=list(a)
i=0
if(i<len(a)):
	b[i],b[i+1]=b[i+1],b[i]
	b[i+2],b[i+3]=b[i+3],b[i+2]
	b=''.join(b)
	print(b)
