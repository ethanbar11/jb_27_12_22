a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []
for item in a:
    for item_b in b:
        if item == item_b and not (item in common):
            common.append(item)

print(common)
