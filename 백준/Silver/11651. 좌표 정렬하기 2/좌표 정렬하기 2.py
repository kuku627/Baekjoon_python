N=int(input())
arr=[]
for i in range(N):
    x,y=map(int,input().split())
    arr.append([x,y])

for i in range(N):
    arr[i][0],arr[i][1]=arr[i][1],arr[i][0]

arr.sort()

for i in arr:
    print(f'{i[1]} {i[0]}')


