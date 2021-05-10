s=input().split("+")
s1=[]
for i in s:
    s1.append(int(i))
s1.sort()
r=str(s1[0])
for i in range (1,len(s1)):
    r=r+'+'+str(s1[i])
print(r)