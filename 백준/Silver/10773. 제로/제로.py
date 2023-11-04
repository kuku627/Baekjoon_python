def calculate_final_sum(K, operations):
    stack = []
    
    for i in range(K):
        num = operations[i]
        if num == 0:
            if stack:
                stack.pop()
            continue
        stack.append(num)
    
    return sum(stack)

# 입력 받기
K = int(input())
operations = []
for _ in range(K):
    num = int(input())
    operations.append(num)

# 최종 합계 계산 및 출력
final_sum = calculate_final_sum(K, operations)
print(final_sum)
