প্রথমে প্রবলেম স্টেট্মেন্ট টা বুঝি একটা এক্সাম্পল এর মাধ্যমে । 
ধরি n=1
(i)তবে আমাদের বের করতে হবে ১ কে ন্যূনতম কত দিয়ে নিঃশেষে ভাগ করা যায় না । সেটা হল 2 . 
তাহলে ans =2 

(*)এখন n=5 হলে -
n=1
n=2
n=3
n=4
n=5

সবগুলোর জন্য (i) এর কাজটা করতে হবে । 
তাহলে --
 
n=1 এর জন্য -- 2
n=2 -->3
n=3 -->2
n=4 -->3
n=5 -->2
ans =  12

এখন আমরা solution procedure এর দিকে আগাই - 
(i) Odd number সবগুলোর জন্য ন্যূনতম কত দিয়ে নিঃশেষে ভাগ করা যায় না সেটা হবে always 2 . 
	তাই প্রথমে ans = ans=n [when n even] or ans = n+1 [when n odd] 

(ii) তাহলে আমার অর্ধেক সংখ্যা কমে গেল । এখন আমার বাকি সংখ্যা থাকল , rest_nums
(iii) 1 এবং 2 lcm হবে 2 . এই ২ দিয়ে কয়টা সংখ্যা ভাগ করা যায় সেগুলো আমরা আগের স্টেপ এই বের করলাম । এখন আমরা বের করব 3 দিয়ে কয়টা সংখ্যাকে ভাগ করতে না পারি । যে কয়টাকে ভাগ করতে পারি না সেগুলোর সাথে ৩ গুন করে ans এ add করে দিব ।
(iv) lcm(2,3) = 6 
এখন আমরা দেখব n এর মধ্যে 6 দ্বারা কয়টা সংখ্যাকে ভাগ করা যায় । সেগুলো res_nums এ থাকবে । বাকিগুলোর জন্যে ন্যূনতম কত দিয়ে নিঃশেষে ভাগ করা যায় না সেটা হল 3 . 
(iv) এরপর ৪ এর জন্য হবে lcm(আগের lcm,4) =12
তাহলে n//12 , এই কয়টা সংখ্যাকে 4 দ্বারা ভাগ করা যায় । 

এভাবে চলতে থাকবে যতক্ষন না পর্যন্ত res_nums 0 হয়ে যাচ্ছে । 


import sys , math
input=sys.stdin.buffer.readline

lcm = lambda a,b: (a*b)//math.gcd(a,b)
for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        ans=n
        rest_nums=n-n//2
    else:
        ans=n+1
        rest_nums=n-(n+1)//2
    a=2
    z=3
    while(rest_nums>0):
        l=lcm(a,z)
        ans+=(rest_nums-n//l)*z
        rest_nums=n//l
        a=l
        z+=1
    print(ans%(1000000007))