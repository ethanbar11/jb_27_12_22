def reverse_string_words(original_string):
    lst = original_string.split(' ')
    final_string = ''
    for i in range(len(lst) - 1, -1, -1):
        final_string = final_string + lst[i] + ' '
    return final_string


lst = ['word1 word2 word3','bli bla blo','la li lo','1 2 3  4 5 6 7 8']
reversed_sentences = []
for sentence in lst:
    reversed_sentences.append(reverse_string_words(sentence))

print(reversed_sentences)