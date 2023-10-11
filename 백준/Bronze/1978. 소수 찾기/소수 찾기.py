

k=int(input())
cnt=0
    
arr=list(map(int,input().split()))
for j in range(len(arr)):
    n=arr[j]

    if n==1:
        continue

    for i in range(2,n+1):
        if n%i==0:
        
            if i==n:
                cnt+=1
                break
            
            break

print(cnt)