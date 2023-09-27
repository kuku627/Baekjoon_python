

N,M=map(int,input().split())

arr=[0]
for i in range(1,N+1):
    arr.append(i)




for i in range(M):
    a,b=map(int,input().split())
    for j in range(a,(((b+a)//2)+1)):
        temp=arr[j]
        arr[j]=arr[b-j+a]
        arr[b-j+a]=temp

for i in range(1,N+1):
    print(arr[i],end=' ')




