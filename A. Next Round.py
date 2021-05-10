
n,k=input().split(" ")
n=int(n)
k=int(k)
lst=input().split(" ")
for i in range(n):
    lst[i]=int(lst[i])

lst.sort()
lst.reverse()
"""list_set=set(lst)
unique_list=(list(list_set))
unique_list.sort()
unique_list.reverse()
a=unique_list[k-1]
"""
a=lst[k-1]
p=0

for i in lst:
    if i>0:
        if i>=a:
            p+=1
print(p)

