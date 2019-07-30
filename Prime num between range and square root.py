a,b=map(int,input().split())
for i in range ((a+1),(b-1)):
	c=0
	for j in range (2,(b-1)):
		if i%j==0:
			c=c+1
	if(c==1):
		print(i,float("{0:.2f}".format(i**0.5)))
		#also we can use ---round(i,2)--- to limit the decimal
