m,n=input().split(" ")
n=int(n)
m=int(m)
x=(n//2)*m
if n%2 !=0 and m>1:
    y=m//2
    print(x+y)
else :
    print(x)


