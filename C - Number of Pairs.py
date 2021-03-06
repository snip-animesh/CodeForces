যে লিস্ট ই থাকুক না কেন প্রথম শর্ত হলো লিস্ট শর্ট করে নিতে হবে । 
এখন আমরা একটা এক্সাম্পল নিইয়ে চিন্তা করি , তাহলে আমাদের বুঝতে সুবিধা হবে । 
5 5 8
1 2 3 4 5

এখানে 1 এর জন্য pair হলো --> (1,4),(1,5)
 2 ---> (2,3),(2,4),(2,5)
 3 ---> (3,4),(3,5)

 4 & 5 এর জন্য কোনো pair সম্বব না । কারন ৪+৫=৯>৮ এবং সব সংখ্যা pair করছে তার ডান দিকের সংখ্যা গুলোর সাথে এবং ৫ এর ডান দিকে কোনো সংখ্যা নেই । 
এখন এখানে , l=5
	 r=8
	x=l-1=4
	y=r-1=7
তাই x হল Lower Limit and y হল Upper Limit.
তাহলে দেখা যাচ্ছে ৪ ও ৭ এর মধ্যে যে সকল সংখ্যা আছে ১ শুধু তাদের সাথেই pair করতে পারবে ।
	x=l-2=3
	y=r-2=6
তাহলে ২ শুধু ৩ ও ৬ এর মধ্যে যে সকল সংখ্যা গুলো আছে তাদের সাথেই pair করতে পারে ।
	x=l-3=2
	y=r-3=5
এখানে Lower limit টা ওই সংখ্যার চেয়ে ছোট হয়ে যাচ্ছে । মানে ৩ এখন ২ এর সাথে একটা pair করবে । বাট  এটা সম্বব না , কারণ ২ , ৩ এর বামদিকে । আর কোনো সংখ্যা তার ডানদিকের সংখ্যা গুলোর সাথেই কেবল pair করতে পারবে। কারণ , (2,3) pair already হয়ে গেছে । তাই Lower limit যদি ওই সংখ্যা (list[i]) এর চেয়ে ছোট হয় তবে Lower limit হিসেবে ওই সংখ্যা টাই বসিয়ে দিব। 
	এখানে x=3
	    y=5
এরপর ৪ এর জন্য - 
	 x=l-4=1  অর্থাৎ =>x=4
	 y=r-4=4
4 & 4 এর মধ্যবর্তী কোনো সংখ্যা নেই । তাই 4 কারো সাথেই pair করতে পারবে না । 

"""Code"""

import bisect
for _ in range(int(input())):
    n,l,r=map(int,input().split())

    lst=sorted([int(x) for x in input().split()])

    sum=0
    for i in range(n-1):
        x=l-lst[i]
        y=r-lst[i]
        if x<=lst[i]:
            x=lst[i]
        p = bisect.bisect_left(lst, x,i+1) #i+1 দিয়ে লিস্টকে i+1 থেকে শেষ পর্যন্ত এতটুকু সাবসেট করে দিলাম । 
        q=bisect.bisect_right(lst,y)
        if q-p>0:
            sum+=(q-p)

    print(sum)
