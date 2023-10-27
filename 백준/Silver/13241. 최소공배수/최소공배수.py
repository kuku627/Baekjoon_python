# 최대공약수(GCD) 계산
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수(LCM) 계산
def lcm(a, b):
    return a * b // gcd(a, b)

# 입력값 A와 B를 받음
A, B = map(int, input().split())

# 최소공배수 계산 및 출력
result = lcm(A, B)
print(result)
