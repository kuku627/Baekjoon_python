x,y,w,h=map(int,input().split())

arr=[]

arr.append(abs(w-x))
arr.append(abs(y-h))
arr.append(abs(x))
arr.append(abs(y))

print(min(arr))