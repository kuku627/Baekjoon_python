# arr=list(input().split('\n'))

# print(arr)

while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break