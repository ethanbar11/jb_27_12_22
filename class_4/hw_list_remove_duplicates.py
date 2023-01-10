list_with_duplicates = [1, 1, 5, 9, 20, 30, 40, 1, 9]

list_without = []

for elem in list_with_duplicates:
    if not (elem in list_without):
        list_without.append(elem)

print(list_without)