T = int(input())


for _ in range(T):
 
    R, S = input().split()
    R = int(R)
    

    P = ''.join([char * R for char in S])
    

    print(P)