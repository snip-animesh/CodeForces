sr=input()
s='hello'
sum=0
j=0
if len(sr)>=5:
    for i in sr:
        if i == s[j]:
            sum+=1
            j+=1
        if sum==5:
            break
    if sum>=5:
        print("YES")
    else:
        print('NO')
else:
    print('NO')
