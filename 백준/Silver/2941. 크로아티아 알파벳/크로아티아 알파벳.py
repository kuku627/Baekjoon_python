word = input()

croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

count = 0  

i = 0
while i < len(word):
    found = False 
    for alphabet in croatian_alphabet:
        if word.startswith(alphabet, i):
            count += 1
            i += len(alphabet) 
            found = True
            break
    if not found:
        count += 1
        i += 1

print(count)





