amt=int(input())
b=input().split()
c=[]
list=''
for i in b:
    if b.count(i)>1 and i not in c:
        c.append(i)
if len(c)>0:
    for i in range(len(c)-1):
        list+=c[i]+" "
    print(list+c[-1])
else:
    print("unique")
