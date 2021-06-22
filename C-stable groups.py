n,k,x=map(int,input().split())
lst=sorted([int(y) for y in input().split()])
if n==1:
    print(1)
else:
    sum=1
    difference_nums=list()
    for i in range(len(lst)-1):
        d=lst[i+1]-lst[i]
        if d>x:
            sum+=1
            difference_nums.append(d)
    difference_nums.sort()
    #where difference is greater than x, there seperated in a new team. Then I
    # have sorted the differences.

    i=0
    while k>0 and i<len(difference_nums):
        new_add_need=(difference_nums[i]-1)//x
        #Here I have counted how many participant needed to add to reduce 1 team.
        if new_add_need<=k:
            k-=new_add_need
            sum-=1
            i+=1
        else:
            break
    print(sum)
