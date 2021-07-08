def light_rad(lst,n,l):
    if 0 in lst:
        rad=lst[1]/2
    else:
        rad=lst[0]

    if l in lst:
        rad1=(l-lst[len(lst)-2])/2
    else:
        rad1=l-lst[len(lst)-1]
    rad= rad if rad>rad1 else rad1

    for i in range(1,len(lst),1):
        rad=rad if (((lst[i]-lst[i-1])/2)<rad) else ((lst[i]-lst[i-1])/2)


    return rad


n,l=map(int,input().split())
lst=[int(x) for x in input().split()]
lst.sort()

if len(lst)==1 and lst[0]==0:
    print(l)
else:
    print(light_rad(lst,n,l))
