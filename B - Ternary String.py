for _ in range(int(input())):
    a=input()
    n=len(a)
    ans=n
    uniqs=set()
    lst=[0]*3
    for i in range(n):
        lst[int(a[i])-1]=i+1
        if a[i] not in uniqs:
            uniqs.add(a[i])
        if len(uniqs)==3:
            ans=min(ans,max(lst)-min(lst)+1)
            
    if len(uniqs)!=3:
        ans=0
    print(ans)
