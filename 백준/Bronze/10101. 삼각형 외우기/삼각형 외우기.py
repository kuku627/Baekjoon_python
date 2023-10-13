a=int(input())
b=int(input())
c=int(input())
cnt=0
if a==b==c:
    cnt=3
elif a==b or b==c or a==c:
    cnt=2
else:
    cnt=1

if a+b+c!=180:
    print("Error")

else:
    if cnt==3:
        print("Equilateral")
    elif cnt==2:
        print("Isosceles")
    else:
        print("Scalene")
