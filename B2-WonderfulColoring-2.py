from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = [int(x) for x in input().split()]
    count = Counter(lst)
    ans= [0] * n
    extras = []
    equal_k={}
    for i, j in count.items():
        if j >= k:
            equal_k[i]=k

    for i in range(n):
        if count[lst[i]]>=k and equal_k[lst[i]]!=0:
            ans[i]=equal_k[lst[i]]
            equal_k[lst[i]]-=1
        elif count[lst[i]]<k:
            extras.append([lst[i],i])
    extras.sort()
# sort না করলে একটা same number একাধিক color হয়ে যেতে পারে । 
    q = len(extras) // k
    x = 0
    for i in range(q):
        for j in range(1, k + 1):
            ans[extras[x][1]] = j
            x += 1
    print(*ans)
