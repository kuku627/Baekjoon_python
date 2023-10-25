import math

# 최대공약수(GCD)를 계산하는 함수
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 최소공배수(LCM)를 계산하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# 테스트 케이스 수 입력
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    result = lcm(a, b)
    print(result)
