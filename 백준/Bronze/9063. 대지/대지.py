n=int(input())

a,b=[],[]

for i in range(n):
    c,d=map(int,input().split())
    a.append(c),b.append(d)


max_a,max_b=max(a),max(b)
min_a,min_b=min(a),min(b)


h=max_a-min_a
w=max_b-min_b

print(h*w)