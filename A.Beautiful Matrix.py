import math
mat=[]
for r in range (5):

    mat1=input().split(" ")
    mat2=[]
    for i in mat1:
        mat2.append(int(i))
    mat.append(mat2)
batti=0
for i in range(5):
    for j in range(5):
        if mat[i][j]==1 :
            x=i+1
            y=j+1
            batti=1
            break;
    if batti==1:
        break

p=abs(3-x)+abs(3-y)
print(p)

