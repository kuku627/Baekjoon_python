import statistics
arr=[]
for i in range(5):
    k=int(input())
    arr.append(k)

arr.sort()
print(statistics.mean(arr))
print(statistics.median(arr))

