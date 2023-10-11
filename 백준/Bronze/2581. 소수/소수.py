

M=int(input())
N=int(input())
# cnt=0
 
arr=[k for k in range(M,N+1)]
arr_prime=[]
# print(arr)
for j in range(len(arr)):
    n=arr[j]

    if n==1:
        continue

    for i in range(2,n+1):
        if n%i==0:
        
            if i==n:
                # cnt+=1
                arr_prime.append(n)
                
                break
            
            break

if len(arr_prime)==0:
    print(-1)
else:
    print(sum(arr_prime))
    print(min(arr_prime))

