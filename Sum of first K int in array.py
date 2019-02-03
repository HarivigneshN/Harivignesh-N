list=[]
n=int(input())
a=int(input())
for i in range (1,n+1):
    b=int(input())
    list.append(b)
b = sum(list[0:a])
print (b)
