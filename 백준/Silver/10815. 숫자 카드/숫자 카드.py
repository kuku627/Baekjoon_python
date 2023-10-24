N = int(input())
sanguen_N = set(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

result = []

for c in card:
    if c in sanguen_N:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))
