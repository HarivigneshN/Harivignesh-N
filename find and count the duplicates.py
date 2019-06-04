a=input().split()
b=[x for n, x in enumerate(a) if x not in a[:n]]
print(b)
c=[x for n, x in enumerate(a) if x in a[:n]]
print(c)
------------------------------------------------------------------------------
l=[1,2,3,4,4,5,5,6,1]
print(set([x for x in l if l.count(x)>1]))
-------------------------------------------------------------------------------
def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  return list( seen_twice )
a = [1,2,3,2,1,5,6,5,5,5]
print(list_duplicates(a))

-------------------------------------------------------------------------------

def dup(a):
    b=[]
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
        else:
            return(a[i])
a=input().split()
print(dup(a))
