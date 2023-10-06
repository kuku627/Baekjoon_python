N=int(input())
sum=0
i=0
while True:
    i+=1
    sum+=i
   
    if sum>=N: break
cnt=N-sum+i-1
k=i+1
#k짝수라인 a+b- -->///  k 홀수라인 <--
# print(cnt)
if k%2==0:
    b=1
    a=k-1
    for i in range(cnt):
        a-=1
        b+=1 

else:
    a=1
    b=k-1
    for i in range(cnt):
        a+=1
        b-=1

print(f'{a}/{b}')
# N=int(input())
# a,b=1,1
# now_layer=1
# now=1
# for k in range(N):
#     now_layer+=1
#     if now_layer%2==0:
#         b+=1
#         now+=1
#         if now==N:
#             break
#         for i in range(now_layer-1):
#             a+=1
#             b-=1
#             now+=1
#             if now==N:
#                 break

#     else: 
#         a+=1
#         now+=1
#         if now==N:
#             break

#         for i in range(now_layer-1):
#             a-=1
#             b+=1
#             now+=1
#             if now==N:
#                 break

# print(f'{a}/{b}')