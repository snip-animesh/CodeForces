s,n=map(int,input().split())
lst=list()
for i in range(n):
    x=[int(y) for y in input().split()]
    lst.append(x)
for i in range(len(lst)):
    x = 0
    for item in lst:

        if item[0]<s:
            s=s+item[1]
            lst.remove(item)
            x=1

    if x==0 or len(lst)==0:
        break
if len(lst)==0:
    print("YES")
else:
    print("NO")





