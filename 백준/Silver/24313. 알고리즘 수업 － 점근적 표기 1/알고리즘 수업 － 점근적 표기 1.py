a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# f(n)가 c * n 이상인지 검사
def satisfies_O_n(a1, a0, c, n0):
    for n in range(n0, 101):  # n0부터 100까지 검사
        if a1 * n + a0 > c * n:
            return 0
    return 1

result = satisfies_O_n(a1, a0, c, n0)
print(result)