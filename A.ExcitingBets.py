import sys
input=sys.stdin.buffer.readline

for _ in range(int(input())):
    a,b=map(int,input().split())
    diff=abs(a-b)
    #a and b এর maximum gcd হতে পারে এদের difference.
    if diff==0:
        print(0,0)
    else:
        step=a%diff
        step=min(abs(diff-step),step)
        #abs(diff-step) --> এখানে diff এর সাথে কত যোগ করে সেটাকে diff দ্বারা divisible করা হইছে তা বের করা হইছে ।
        #step --> এটা হল diff এর সাথে কত বিয়োগ করে সেটাকে diff দ্বারা divisible করা হইছে তা বের করা হইছে ।
        print(diff,step)
