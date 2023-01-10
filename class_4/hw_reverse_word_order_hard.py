text = 'My name is Ethan'

lst = []
word = ''
for character in text:
    if character != ' ':
        word = word + character
    else:
        lst.append(word)
        word = ''
lst.append(word)
# print(lst)
final_string = ''
for i in range(len(lst) - 1, -1, -1):
    final_string = final_string +lst[i] + ' '

print(final_string)