
a,b=[],[]
for i in range(3):
    n,m=map(int,input().split())
    a.append(n),b.append(m)


if a[0]==a[1]:
    c=a[2]
elif a[0]==a[2]:
    c=a[1]
elif a[1]==a[2]:
    c=a[0]

if b[0]==b[1]:
    d=b[2]
elif b[0]==b[2]:
    d=b[1]
elif b[1]==b[2]:
    d=b[0]

print(f"{c} {d}")

