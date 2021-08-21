# First we make a array of all powers of 2 till 10**9
powers_two=[str(2**i) for i in range(64)]
# Create a function which will return how many digits need to pop or insert from n to make i
def difference(n,s):
    counter=0
    iterator=0
    for j in n:
        if j==s[iterator]:
            counter+=1
            iterator+=1
            if iterator==len(s):
                break
    return len(n)+len(s)-2*counter


for _ in range(int(input())):
    n=input()
    print(min([difference(n,i) for i in powers_two]))
