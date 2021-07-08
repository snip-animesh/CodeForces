#code 1 - collected
n,a,b,c=map(int,input().split())
z=[0]+[-10]*10
print(z)
for i in range(1,n+1):
    z[i]=max(z[i-a],z[i-b],z[i-c])+1
    print(z[i-a])
    print(z[i-b])
    print(z[i-c])
    print(z[i],i)
print(z[n])

#code 2 - collected
n, a, b, c = map(int, input().split())

dp = [-5000 for i in range(n + 1)]
dp[0] = 0
for i in range(1, n + 1):
    for x in (a, b, c):
        if i - x >= 0:
            dp[i] = max(dp[i], dp[i - x] + 1)

print(dp[n])

#code 3- I did

def funk(n,a,b,c):
    result=0
    for x in range(4001):
        for y in range(4001):
            rest=n-(x*a+y*b)
            if rest<0:
                break
            elif rest%c==0:
                score=x+y+(rest//c)
                result=max(result,score)


    return result

n,a,b,c=[int(x) for x in input().split()]

print(funk(n,a,b,c))
