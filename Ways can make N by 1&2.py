a=int(input())
b=0
for x in range(0,a+1):
	for y in range(0,a+1):
		c=1*x+2*y
		if c==a:
			b=b+1
print(b)
