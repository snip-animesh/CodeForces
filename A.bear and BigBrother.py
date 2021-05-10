a,b=input().split()
a,b=int(a),int(b)
sum=0
for i in range(10):
    if a<=b:
        a=a*3
        b=b*2
        sum+=1
    if a>b:
        break
print(sum)