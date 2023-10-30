import math

# 최대 공약수(GCD)를 구하는 함수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 입력값 받기
n = int(input())
tree_positions = [int(input()) for _ in range(n)]

# 인접한 가로수 간의 간격을 계산하고 최대 공약수를 구함
distances = [tree_positions[i + 1] - tree_positions[i] for i in range(n - 1)]
common_gcd = distances[0]
for distance in distances:
    common_gcd = gcd(common_gcd, distance)

# 모든 가로수 간의 간격을 같게 만들기 위해 필요한 추가 가로수의 수 계산
total_trees = sum(distance // common_gcd - 1 for distance in distances)

print(total_trees)
