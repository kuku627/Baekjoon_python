
N=int(input())

for i in range(1,int(N)+1):
    t=1
    sum=0
    digit=str(i)
    for j in digit:
        sum+=int(j)
    k=sum    
    sum+=i
    if sum==int(N):
        print(sum-k)
        break
    
    t=0
if t==0:
    print(0)

        

    
# sum=0
# digit=input()
# for i in digit:
#     sum+=int(i)


# print(sum)