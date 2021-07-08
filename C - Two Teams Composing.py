for i in range(int(input())):
    n=int(input())
    lst=[int(x) for x in input().split()]
    if len(lst)==1 or len(lst)==0:
        print(0)

    else:
        lst1=[0]*(n+1)
        for x in lst:
            lst1[x]+=1
        maxi=max(lst1)
        index_maxi=lst1.index(maxi)
        if maxi==1:
            print(1)

        else:
            lst=set(lst)
            lst.remove(index_maxi)
            length=len(lst)
            if maxi>length+1:
                print(length+1)
            else:
                print(min(maxi,length))
                
                
 #I used counting sort algorithm to find maximum repeated number. 
