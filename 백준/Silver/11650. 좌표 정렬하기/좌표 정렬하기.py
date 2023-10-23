N=int(input())
arr=[]
for i in range(N):
    x,y=map(int,input().split())
    arr.append([x,y])

arr.sort()

for i in arr:
    print(f'{i[0]} {i[1]}')


