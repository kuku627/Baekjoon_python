def is_valid_parenthesis(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')' and stack:
            stack.pop()
        else:
            return "NO"
    return "NO" if stack else "YES"

T = int(input())
for _ in range(T):
    parenthesis_str = input()
    result = is_valid_parenthesis(parenthesis_str)
    print(result)
