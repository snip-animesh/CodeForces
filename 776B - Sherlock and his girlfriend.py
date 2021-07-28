n=100002
arr=[1]*n
for i in range(2,n):
    if arr[i]==1:
        arr[i]=i
        for j in range(i*i,n,i):
            arr[j]=i

n,d,ans=int(input()),{},[]
nums=list(range(2,n+2))
for i in nums:
    lst=set()
    while(i>1):
        lst.add(arr[i])
        i//=arr[i]
    if i>=2:
        lst.add(i)
        #lst is the prime factors of i
    k=1
    for j in lst:
        if j in d.keys():
            if d[j]==k:
                k+=1
        else:
            d[j]=k
    ans.append(k)
print(len(set(ans)))
print(*ans)
