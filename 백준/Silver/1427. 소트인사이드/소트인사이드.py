n=int(input())

k=str(n)
arr=[]
for i in range(len(k)):
    arr.append(int(k[i]))


arr.sort(reverse=True)

for i in range(len(arr)):
    print(arr[i],end='')