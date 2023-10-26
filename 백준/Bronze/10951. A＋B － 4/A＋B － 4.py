while True:
    try:
        a, b = map(int, input().split())
        result = a + b
        print(result)
    except EOFError:
        break
