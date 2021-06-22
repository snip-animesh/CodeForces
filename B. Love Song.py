n,q=map(int,input().split())
s=input()
lst=[0]
ss=0
for i in s:
    ss+=ord(i)-96
    lst.append(ss)

for _ in range(q):
    l, r = map(int, input().split())
    print(lst[r]-lst[l-1])

# s=abacaba
# lst=[0,1,3,4,7,8,10,11]
# l=1,r=3
# Ans=4-0
# l=2,r=5
# sub_string=baca
# Ans_string=bbaccca
# Ans=8-1=7
