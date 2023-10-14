N = int(input())

group_word_count = 0

for _ in range(N):
    word = input()
    used_letters = set()
    is_group_word = True

    for i in range(len(word)):
        letter = word[i]
        if i > 0 and letter != word[i - 1]:
            if letter in used_letters:
                is_group_word = False
                break
        used_letters.add(letter)

    if is_group_word:
        group_word_count += 1

print(group_word_count)
