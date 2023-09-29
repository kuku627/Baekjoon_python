positions = [-1] * 26

S = input()
for i in range(len(S)):
    index = ord(S[i]) - ord('a')
    if positions[index] == -1:
        positions[index] = i
        
for pos in positions:
    print(pos, end=' ')