lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_counter = 0
even_counter = 0

odd_lst = []
even_lst = []
for i in lst:
    if i % 2 == 0:
        even_counter += 1 # even_counter = even_counter +1
        even_lst.append(i)
    else:
        odd_counter += 1
        odd_lst.append(i)
print('Number of odd values found: ', odd_counter, 'and the numbers are:', odd_lst)
print('Number of even values found: ', even_counter, 'and the numbers are:', even_lst)
