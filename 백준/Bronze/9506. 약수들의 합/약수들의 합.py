
n=1

while(True):
    arr=[]
    n=int(input())
    if n==-1:
        break
    for i in range(1,n):
        if n%i==0:
            arr.append(i)
            # print(arr)
            # print(lend(arr))
    if sum(arr)==n:
        print(f"{sum(arr)} = {arr[0]}",end='')
        for k in range(1,len(arr)):
            print(f" + {arr[k]}",end='')
        print()     
    else:
        print(f"{n} is NOT perfect.")

  
