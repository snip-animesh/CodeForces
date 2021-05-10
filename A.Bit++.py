X=0
n=int(input())
for i in range (n):
    s=input()
    if s=='++X' or s=='X++':
        X+=1
    if s=='--X' or s== 'X--':
        X-=1
print(X)