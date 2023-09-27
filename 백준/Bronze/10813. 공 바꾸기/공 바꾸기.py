N,M=map(int,input().split())
arr=[0]
for i in range(1,N+1):
    arr.append(i)



for i in range(M):
    a,b=map(int,input().split())
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp


for i in range(1,N+1):
    print(arr[i],end=' ')