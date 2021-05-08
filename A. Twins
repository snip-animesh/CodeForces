n=int(input())
#s=input()
lst1=[]
lst1.append(input().split(" "))
#print(len(lst1))
lst=[]

for i in range(n):
    lst.append(int(lst1[0][i]))
#print(lst)
lst.sort()
lst.reverse()
#print(lst)
sum=0
for i in lst:
    sum=sum+i
result=0
coin=0
#print(sum)
for i in lst:
    if result>sum:
        break
    else:
        sum=sum-i
        result=result+i
        #print(sum)
        coin+=1
        #print(coin)
print(coin)
