import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

sorted_numbers = sorted(numbers)

for number in sorted_numbers:
    print(number)