def sieve_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p ** 2 <= n:
        if is_prime[p]:
            for i in range(p ** 2, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def count_goldbach_partitions(N, primes):
    count = 0
    i, j = 0, len(primes) - 1
    while i <= j:
        if primes[i] + primes[j] == N:
            count += 1
            i += 1
            j -= 1
        elif primes[i] + primes[j] < N:
            i += 1
        else:
            j -= 1
    return count

primes = sieve_eratosthenes(1000000)  # 1,000,000 이하의 소수를 미리 구합니다.

T = int(input())
for _ in range(T):
    N = int(input())
    partitions = count_goldbach_partitions(N, primes)
    print(partitions)
