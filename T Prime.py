all_nums=[1]*1000000
final_nums=set()
for i in range(2,1000000):
    if all_nums[i]:
        final_nums.add(i*i)
        for j in range(i*i,1000000,i):
            all_nums[j]=0
input()
for x in map(int,input().split()):
    if x in final_nums:
        print("YES")
    else:
        print("NO")
