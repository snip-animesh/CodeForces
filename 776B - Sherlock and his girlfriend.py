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


"""আরেকটা সহজ লজিক । সব কম্পোজিট নাম্বার গুলোর জন্য ২ হবে আর প্রাইম নাম্বার গুলোর জন্য ১ """

n=int(input())+2
ans=[1]*n
for i in range(2,n):
    for j in range(i*i,n,i):
        ans[j]=2
print(len(set(ans[2:])))
print(*ans[2:])
