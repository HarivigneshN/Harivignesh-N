l=[]
n_array=int(input())
a_integer=int(input())
for i in range (1,n_array+1):
    b=int(input())
    l.append(b)
c = sum(l[0:a_integer])
print (c)
