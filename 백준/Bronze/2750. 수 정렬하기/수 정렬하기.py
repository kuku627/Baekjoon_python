N=int(input())
arr=[]
for i in range(N):
    k=int(input())
    arr.append(k)

arr.sort()

for i in range(N):
    print(arr[i],end='\n')
          