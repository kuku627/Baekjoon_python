
T=int(input())
coin=[0]*4
for i in range(T): # 194  175
    a=int(input())
    coin[0]=int(a/25)
    coin[1]=int(int(a%25)/10)
    coin[2]=int((int(a%25)%10)/5)
    coin[3]=int((a%5)/1)
    print(f'{coin[0]} {coin[1]} {coin[2]} {coin[3]}')