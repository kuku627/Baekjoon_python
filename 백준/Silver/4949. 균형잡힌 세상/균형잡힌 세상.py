while True:
    line = input().rstrip()
    
    if line == '.':
        break
    
    stack = []
    balanced = True
    
    for char in line:
        if char in '()[]':
            if char in '([':
                stack.append(char)
            else:
                if not stack or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '['):
                    balanced = False
                    break
                stack.pop()
    
    if not stack and balanced:
        print("yes")
    else:
        print("no")
