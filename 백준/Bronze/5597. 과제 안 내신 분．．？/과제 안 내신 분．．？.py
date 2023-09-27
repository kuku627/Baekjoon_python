arr=[0]*31

for i in range(1,29):
    a=int(input())
    arr[a]=a

for i in range(1,31):
    if arr[i]==0:
        print(i)