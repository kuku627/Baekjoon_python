from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 주어진 N개의 수로 만들 수 있는 모든 순열 생성
permutation_list = list(permutations(numbers, M))

# 사전 순으로 정렬
permutation_list.sort()

# 결과 출력
for permutation in permutation_list:
    for num in permutation:
        print(num, end=' ')
    print()
