from collections import Counter
n=2000001
arr=[1]*n
for i in range(2,n):
    if arr[i]==1:
        arr[i]=i
        for j in range(i*i,n,i):
            arr[j]=i

n=int(input())
dfs=set()
primefacts=[]
lst=[int(x) for x in input().split()]
for i in lst:
    pfs=[]
    if i==1:
        pfs.append(1)
        dfs.add(i)
    else:
        while(i>1):
            pfs.append(arr[i])
            dfs.add(arr[i])
            i//=arr[i]
        if i>=2:
            pfs.append(i)
            dfs.add(arr[i])
    primefacts.append(Counter(pfs))
# print(primefacts)
ans=1
for i in dfs:
    powers=[]
    for j in primefacts:
        if j[i]:
            powers.append(j[i])
    powers.sort()
    if len(powers)==n:
        ans*=pow(i,powers[1])
    elif len(powers)==n-1:
        ans*=pow(i,min(powers))
print(ans)
