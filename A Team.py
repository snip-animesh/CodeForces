n=int(input())
ps=0
for i in range(n):
    sum=0
    a,b,c=input().split(" ")
    a=int(a)
    b=int(b)
    c=int(c)
    if a==1:
        sum+=1
    if b==1:
        sum+=1
    if c==1:
        sum+=1
    if sum>=2:
        ps+=1
print(ps)
