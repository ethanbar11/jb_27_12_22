non_printable_numbers = [1, 40, 39, 50]
for i in range(100):
    should_print_number = True
    for x in non_printable_numbers:
        if x == i:
            should_print_number = False
            break

    if should_print_number == True:
        print(i)
