N=int(input())

arr=list(map(int,input().split()))
max=max(arr)
for i in range(N):
    arr[i]=arr[i]/max*100

# print(arr)
print(sum(arr)/len(arr))