s=input()
s=s.lower()
#s="Hello"
fs=""
v=['a','e','i','o','u','y']
for i in s:
    for j in v:
        if i==j:
            s=s.replace(i,'')
l=len(s)
for i in range(l-1,-1,-1):
    fs=fs+s[i]
    fs=fs+'.'

fs=fs[::-1]
print(fs)
