N=int(input())
A=[]
for i in range(100):
    row = []
    for j in range(100):
        row.append(0)
    A.append(row)
# A = [[0 for j in range(100)] for i in range(100)]

for k in range(N):
    a,b=map(int,input().split())
    for i in range(10):
        for j in range(10):
            A[a+i][b+j]=1

sum=0
for i in range(100):
    for j in range(100):
        if A[i][j]==1:
            sum+=1
print(sum)