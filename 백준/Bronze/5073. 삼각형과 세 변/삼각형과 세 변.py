while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    cnt=0
    if a==b==c:
        cnt=3
    elif a==b or b==c or a==c:
        cnt=2
    else:
        cnt=1
    arr=[a,b,c]
    arr=sorted(arr)
    a,b,c=arr[0],arr[1],arr[2]
    if a+b<=c:
        print("Invalid")

    else:
        if cnt==3:
            print("Equilateral")
        elif cnt==2:
            print("Isosceles")
        else:
            print("Scalene")
