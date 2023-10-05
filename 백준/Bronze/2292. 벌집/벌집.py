
N=int(input())
i=0
now_number,now_layer=1,1
if N==1:
    print(N)

else:
    while True:
        i+=1
        now_layer+=1
        now_number+=6*i
        if N<=now_number:
            print(now_layer)
            break
        else: continue






# 밑에꺼 내가 풀고 메모리 불가
# b=1
# N=int(input())
# a=[[1]]
# for i in range(1,100):
#     row=[]
#     for j in range(i*6):
#         b+=1
#         row.append(b)
#     if(b==N):
#         break 
#     a.append(row)
    
# for i in range (len(a)):
#     if N in a[i]:
#         index = i
#         break


# print(index+1)