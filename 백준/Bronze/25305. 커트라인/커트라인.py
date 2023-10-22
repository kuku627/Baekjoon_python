N,k=map(int,input().split())
N=list(map(int,input().split()))

N.sort(reverse=True) 

print(N[k-1])

