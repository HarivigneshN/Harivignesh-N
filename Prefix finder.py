z=int(input())
a=[]
for i in range (0,z):
    b=input()
    a.append(b)
c=[]    
for i in zip(*a):
	if i.count(i[0])==len(i):
		c.append(i[0])
	else:
		break
print(''.join(c))
