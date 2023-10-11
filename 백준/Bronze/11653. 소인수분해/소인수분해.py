n=int(input())
new_num=n
arr=[]

while new_num>=2:

    for i in range(2,new_num+1):
        if new_num%i==0:
            new_num=new_num//i
            arr.append(i)
            break

for i in range(len(arr)):
    print(arr[i])