import math

# 두 분수의 분모가 같아지도록 변환
def make_common_denominator(a, b):
    lcm = a[1] * b[1] // math.gcd(a[1], b[1])
    a = (a[0] * (lcm // a[1]), lcm)
    b = (b[0] * (lcm // b[1]), lcm)
    return a, b

# 두 분수를 더하여 기약분수로 반환
def add_fractions(a, b):
    a, b = make_common_denominator(a, b)
    result = (a[0] + b[0], a[1])
    gcd = math.gcd(result[0], result[1])
    return (result[0] // gcd, result[1] // gcd)

# 입력값 받기
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

# 분수 덧셈
result = add_fractions(a, b)

# 결과 출력
print(result[0], result[1])
