l=[4,44,47,474,477,444,447,7,74,77,774,744,777,747]

n=int(input())
batti=1
for i in l:
    if n%i==0:
        print("YES")
        batti=0
        break
if batti == 1:
    print("NO")