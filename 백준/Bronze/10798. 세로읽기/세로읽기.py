
A=[]
max_len=[]
for i in range(5):
    row=input()
    A.append(row)

for i in range (5):
    max_len.append(len(A[i]))


# 0 0 10 20 30 40 ///01 11 21 31 41  60 61 62  64
for i in range(max(max_len)):
    for j in range(5):
        try: 
            if(A[j][i]<='z'and A[j][i]>='a')or(A[j][i]<='Z'and A[j][i]>='A')or(A[j][i]<='9' and A[j][i]>='0'):
                print(A[j][i],end='')
        except IndexError:
            continue
    
   
    #    if i < len(A[j]) and ((A[j][i] <= 'z' and A[j][i] >= 'a') or (A[j][i] <= 'Z' and A[j][i] >= 'A') or (A[j][i] <= '9' and A[j][i] >= '0')):
    #         print(A[j][i], end='')

   