import math
n=int(input())
lst=[int(x) for x in input().split()]
lst1,lst2,lst3,lst4=[],[],[],[]
for i in lst:
    if i==1:
        lst1.append(i)
    elif i==2:
        lst2.append(i)
    elif i == 3:
            lst3.append(i)
    else:
        lst4.append(i)
#Seperated 1,2,3,4 in 4 different lists.
taxi=len(lst4)
#print(lst4)
#print(taxi)
if len(lst3)>=len(lst1):
    taxi=taxi+len(lst3)+math.ceil((len(lst2))/2)
else:
    taxi=taxi+len(lst3)                 #Num of 3's taxi is added
    l1=len(lst1)-len(lst3)              #Rest Num of 1 in l1
    taxi=taxi+(l1//4)                   #Taxi required for 4 1's
    r1=l1%4                             #Rest 1's
    taxi=taxi+(len(lst2))//2            #Taxi for 2's
    r2=(len(lst2))%2                    #Rest 2's
    taxi=taxi+math.ceil((r1+(r2*2))/4)  #Taxi required for rest 1 and 2's together
print(taxi)

