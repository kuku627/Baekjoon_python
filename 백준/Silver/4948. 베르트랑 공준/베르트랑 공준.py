# Define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Generate prime numbers up to a given limit using the Sieve of Eratosthenes
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return [i for i in range(2, limit + 1) if sieve[i]]

# Main function to count prime numbers in the given range
while True:
    n = int(input())
    if n == 0:
        break
    primes = generate_primes(2 * n)
    count = sum(1 for p in primes if n < p <= 2 * n)
    print(count)
