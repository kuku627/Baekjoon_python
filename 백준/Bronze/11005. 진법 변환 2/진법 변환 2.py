
n, b = map(int, input().split())
result = ""

while n > 0:
    remainder = n % b
    if remainder < 10:
        result = str(remainder) + result
    else:
        result = chr(ord('A') + (remainder - 10)) + result
    n //= b

print(result)

# n, b = map(int, input().split())
# result_list = []

# while n > 0:
#     remainder = n % b
#     if remainder < 10:
#         result_list.insert(0, str(remainder))
#     else:
#         result_list.insert(0, chr(ord('A') + (remainder - 10)))
#     n //= b

# result = ''.join(result_list)
# print(result)