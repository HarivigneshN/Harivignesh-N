a = input()
b = 1
for i in a:
	if a.count(i)>b:
		b=a.count(i)
		c=i
print(c)		
