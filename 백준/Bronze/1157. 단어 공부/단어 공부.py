word = input().upper()  
word_count = {}  
for char in word:
    if char in word_count:
        word_count[char] += 1
    else:
        word_count[char] = 1

max_count = max(word_count.values())
most_common_chars = [char for char, count in word_count.items() if count == max_count]

if len(most_common_chars) > 1:
    print("?")
else:
    print(most_common_chars[0])