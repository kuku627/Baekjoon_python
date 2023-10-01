total_time=0
alp=input()
for i in alp:
       
    if 'A' <= i <= 'C':
        total_time += 3
    elif 'D' <= i <= 'F':
        total_time += 4
    elif 'G' <= i <= 'I':
        total_time += 5
    elif 'J' <= i <= 'L':
        total_time += 6
    elif 'M' <= i <= 'O':
        total_time += 7
    elif 'P' <= i <= 'S':
        total_time += 8
    elif 'T' <= i <= 'V':
        total_time += 9
    elif 'W' <= i <= 'Z':
        total_time += 10
print(total_time)